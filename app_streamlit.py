
import streamlit as st
import pandas as pd

# Titre de l'application
st.title("Prédiction du Prix des Maisons")

# Champs de saisie pour les variables clés
sqft = st.number_input("Surface habitable (sqft)")
bedrooms = st.number_input("Nombre de chambres", step=1)

# Bouton de soumission
if st.button("Prédire"):
    st.write(f"Surface : {sqft}, Chambres : {bedrooms}")
    st.write("Prédiction fictive : 500000")
