import streamlit as st
from src.router import redirect

def load_view():
    
    st.markdown("""
        
    Analyser les critères qui différencient les planètes entre elles.

    Problématique : quelle est la planète la plus étrangère à la Terre ?

    Le dataset contient les planètes principales du système solaire (sans les "planètes naines") représentées dans les lignes au nombre de 8.
     Puis 22 colonnes contenant des critères départageant les lignes selon des mesures et caractéristiques différentes.

    Pour chaque critère :

    Comparer les valeurs à celle de la Terre, et interpréter ce que cela implique pour la planète la plus différente.
        
    """)

    if st.button("données"):
            redirect("/données", reload=True)
