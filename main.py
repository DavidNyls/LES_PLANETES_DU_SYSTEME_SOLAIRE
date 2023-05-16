import streamlit as st
from src.views import login, home, objectif, dataset, analyse, conclusion
from src.router import redirect, get_route
from src.models.cookie import Cookie
from src.controllers.auth import logout

import utils as utl
st.set_page_config(page_title='Navbar sample')
st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()

def navigation():


    route = get_route() # récupères la route actuelle
    # contrôle de cookie
    c = Cookie("data.json")
    valuesCookie = dict(c.read())

    # force la connection de l'utilisateur
    if valuesCookie["uid"] == None and route != "/login":
        redirect("/login", reload=True)

    
    #systeme de routes
    if route == "/login":
        if valuesCookie["uid"] != None:
            redirect("/home", reload=True)
        else:
            login.load_view() # on renvoie vers la vue login
         # on charge la vue login

    elif route == "/home": # on renvoie vers la vue home
        home.load_view() # on charge la vue home

    elif route == "/objectif":
        objectif.load_view()

    elif route == "/données":
        dataset.load_view()

    elif route == "/analyse":
        analyse.load_view()

    elif route == "/conclusion":
        conclusion.load_view()

    elif route == "/logout":
        logout()
        redirect("/login", reload=True)

    else: # si la route n'existe pas 
        redirect("/login") # renvoie au login
        home.load_view()
        #navigation() # recommence

navigation()