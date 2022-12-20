import streamlit as st
from src.controllers.auth import login
from src.router import redirect

def load_view():

    st.title("Les Planètes du système Solaire (Dataset)")

    st.header("Page de Connexion")

    email = st.text_input("Email")
    password = st.text_input("Mot de passe", type="password")
    

    if st.button("Se connecter") == False:
        st.warning("Veuillez entrer votre email et votre mot de passe")
    else:
        res = login(email, password)
        if res:
            st.success("Bienvenue !", icon="✅")
            redirect("/home", True)
        else:
            st.error("Email ou mot de passe incorrect(s)")

