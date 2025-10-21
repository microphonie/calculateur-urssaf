import streamlit as st

st.set_page_config(page_title="Calculateur brut vers net", page_icon="logo_UVPC.png")
st.image("logo_UVPC.png", width=400)
st.title("Calculateur brut vers net - micro-entreprise")
st.write("Cet outil permet de déduire les cotisations URSSAF du salaire brut.")

mode = st.radio(
    "Type de conversion",
    ("Brut vers net", "Combien d'heures dois-je faire pour tel salaire net ?", "Heures restantes avec objectif annuel")
)

import datetime
from datetime import datetime
 
month = datetime.now().month
year = datetime.now().year
 
urssaf = 25.6

def salaire_mensuel_net(mensuel_brut, urssaf):
    return mensuel_brut * (1 - urssaf / 100)

def prelev_urssaf(mensuel_brut, urssaf):
    return mensuel_brut * (urssaf / 100)

def obj_salaire_brut(mensuel_net):
    return mensuel_net / (1 - urssaf / 100)

def obj_salaire_heures(mensuel_brut):
    return (mensuel_brut / 65) / 4

if mode == "Brut vers net":
    mensuel_brut = st.number_input(
        "Salaire mensuel brut :",
        min_value=0.0, step=0.5, format="%.2f"
    )
    if mensuel_brut > 0:
        mensuelnet = salaire_mensuel_net(mensuel_brut, urssaf)
        prel_urssaf = prelev_urssaf(mensuel_brut, urssaf)

        st.success(f"Salaire mensuel net (après déduction URSSAF) : **{mensuelnet:.2f} €**")
        st.info(f"Prélèvement URSSAF : **{prel_urssaf:.2f} €**")
        st.caption("Calcul basé sur le taux de prélèvement URSSAF au 1er janvier 2025 : 25,6.")

elif mode == "Combien d'heures dois-je faire pour tel salaire net ?":
    objectif_mensuel = st.number_input(
        "Salaire mensuel net à atteindre :",
        min_value=0.0, step=0.5, format="%.2f"
    )
    if objectif_mensuel > 0:
        objectif_salaire_brut = obj_salaire_brut(objectif_mensuel)
        objectif_salaire_heures = obj_salaire_heures(objectif_salaire_brut)

        st.success(f"Heures hebdomadaires à réaliser (basées sur forfait 65€/h) : **{objectif_salaire_heures:.2f} h**")
        st.success(f"Salaire brut mensuel à faire : **{objectif_salaire_brut:.2f} €**")
        st.caption(f"Calcul basé sur le taux de prélèvement URSSAF au 1er janvier 2025 : 25,6.")

elif mode == "Heures restantes avec objectif annuel":
    mode = st.radio(
    "Année civile ou scolaire ?",
    ("Septembre à septembre", "Janvier à Janvier")
    )
    objectif_mensuel = st.number_input(
        "Salaire mensuel net à atteindre :",
        min_value=0.0, step=0.5, format="%.2f"
    )
    ca_brut = st.number_input(
    "Chiffre d'affaires brut déjà réalisé depuis septembre :",
    min_value=0.0, step=0.5, format="%.2f"
    )
    if mode == "Septembre à septembre":
        mois_restants = 9 - month
    if mode == "Janvier à janvier":
        mois_restants = 12 - month

    if objectif_mensuel and ca_brut > 0:
        objectif_salaire = (objectif_mensuel * 12) - (ca_brut * (1 - urssaf / 100))
        heures_restantes_total = objectif_salaire / 65
        heures_restantes_hebdo = heures_restantes_total / (mois_restants * 4)
        st.success(f"Salaire brut restant à faire : **{objectif_salaire:.2f} €**")
        st.success(f"Heures totales restantes à faire (basées sur forfait 65€/h) : **{heures_restantes_total:.2f} h**")
        st.info(f"Heures hebdo restantes à faire jusqu'à la fin de l'année : **{heures_restantes_hebdo:.2f} h**")
        st.caption(f"Calcul basé sur le taux de prélèvement URSSAF au 1er janvier 2025 : 25,6.")
        st.caption(f"**{month} {year}**")