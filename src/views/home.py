import streamlit as st
from src.router import redirect
from src.controllers.auth import logout

def load_view():
    st.title('Les Planètes du Système Solaire')
    st.markdown("Accueil")

    if st.button("Login"):
            redirect("/login", reload=True)

    if st.button("Déconnexion"):
        logout()
        redirect("/login", reload=True)

    if st.button("objectif"):
        redirect("/objectif", reload=True)