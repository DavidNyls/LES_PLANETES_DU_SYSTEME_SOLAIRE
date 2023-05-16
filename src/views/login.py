import streamlit as st
from src.controllers.auth import login
from src.router import redirect

"""def check_password_strength(password):
    # Longueur minimale de 12 caractères
    if len(password) < 12:
        return "Le mot de passe doit contenir au moins 12 caractères."

    # Au moins une lettre majuscule
    if not any(c.isupper() for c in password):
        return "Le mot de passe doit contenir au moins une lettre majuscule."

    # Au moins une lettre minuscule
    if not any(c.islower() for c in password):
        return "Le mot de passe doit contenir au moins une lettre minuscule."

    # Au moins un chiffre
    if not any(c.isdigit() for c in password):
        return "Le mot de passe doit contenir au moins un chiffre."

    # Au moins un caractère spécial
    if not any(c in "!@#$%^&*()" for c in password):
        return "Le mot de passe doit contenir au moins un caractère spécial (par exemple, !@#$%^&*)."

    return """

def load_view():

    st.title("Les Planètes du système Solaire (Données)")

    st.header("Page de Connexion")

    email = st.text_input("Email")
    password = st.text_input("Mot de passe", type="password")
    

    if st.button("Se connecter") == False:
        st.warning("Veuillez entrer votre email et votre mot de passe")
        st.warning("Il est conseillé de choisir un mot de passe long et complexe, en évitant la réutilisation des anciens mots de passe")
    else:
        res = login(email, password)
        if res:
            st.success("Bienvenue !", icon="✅")
            redirect("/home", True)
        else:
            st.error("Email ou mot de passe incorrect(s)")


