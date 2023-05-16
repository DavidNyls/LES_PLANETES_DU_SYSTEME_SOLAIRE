import streamlit as st
from src.router import redirect
import pandas as pd
import sqlite3 as sqlite
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import math
import plotly.graph_objects as go


def spheres(size, clr, dist=0): 
    
    # Set up 100 points. First, do angles
    theta = np.linspace(0,2*np.pi,100)
    phi = np.linspace(0,np.pi,100)
    
    # Set up coordinates for points on the sphere
    x0 = dist + size * np.outer(np.cos(theta),np.sin(phi))
    y0 = size * np.outer(np.sin(theta),np.sin(phi))
    z0 = size * np.outer(np.ones(100),np.cos(phi))
    
    # Set up trace
    trace= go.Surface(x=x0, y=y0, z=z0, colorscale=[[0,clr], [1,clr]])
    trace.update(showscale=False)

    return trace

def orbits(dist, offset=0, clr='white', wdth=2): 
    
    # Initialize empty lists for eac set of coordinates
    xcrd=[]
    ycrd=[]
    zcrd=[]
    
    # Calculate coordinates
    for i in range(0,361):
        xcrd=xcrd+[(round(np.cos(math.radians(i)),5)) * dist + offset]
        ycrd=ycrd+[(round(np.sin(math.radians(i)),5)) * dist]
        zcrd=zcrd+[0]
    
    trace = go.Scatter3d(x=xcrd, y=ycrd, z=zcrd, marker=dict(size=0.1), line=dict(color=clr,width=wdth))
    return trace

def annot(xcrd, zcrd, txt, xancr='center'):
    strng=dict(showarrow=False, x=xcrd, y=0, z=zcrd, text=txt, xanchor=xancr, font=dict(color='white',size=12))
    return strng

def load_view():

    st.markdown("""

## Conclusion

On distingue clairement deux grandes catégories de planètes : les planètes "telluriques" et les planètes "gazeuses". Dans le Système solaire, Mercure, Vénus, la Terre et Mars sont des planètes telluriques alors que Jupiter, Saturne, Uranus et Neptune sont des planètes gazeuses. La nébuleuse de gaz primitive à l'origine de la naissance des planètes du Système solaire était majoritairement composée d'hydrogène et d'hélium, tout comme l'est le reste de l'univers (l'hydrogène étant l'élément le plus abondant). Cependant, sous l'effet de divers phénomènes physiques, ces éléments ont migré vers l'extérieur du système. Les planètes internes du Système solaire, les planètes telluriques, sont essentiellement formées de minéraux et de roches qui s'organisent en trois enveloppes concentriques : le noyau, le manteau et la croûte. Leur densité est comprise entre 4 et 6 grammes au cm cube contrairement aux planètes gazeuses comportant une densité proche de celle de l'eau (autour de 1gr/cm³).

Privées de la majeure partie de la matière disponible dans la nébuleuse primitive, les planètes telluriques sont de tailles modestes comparées à celles qu'affichent les planètes gazeuses, également surnommées planètes géantes : 12756 km de diamètre pour la Terre contre quelque 142 984 km pour Jupiter. Du fait de leurs tailles modestes, les planètes telluriques, contrairement aux planètes gazeuses, n'ont pas été capables de s'orner d'anneaux ni de retenir un grand nombre de satellites.

Également dans les différences notables, la période de rotation et autres variantes dans la mécanique céleste comme les inclinaisons orbitales, l'excentricité etc... sont autant de marqueurs de différences pour perturber nos repères terrestres. Cependant, par-delà leurs oppositions, les planètes s'influencent les unes par rapport aux autres et demeurent irrémédiablement connectées. Les planètes de notre système et leurs mystères, n'ont de cesse de faire bouillonner les esprits les plus brillants, alimentant leurs contradictions dans une fabuleuse danse mathématique et physique.

    
    """)

    # Note, true diameter of the Sun is 1,392,700km. Reduced it for better visualization
    diameter_km = [200000, 4879, 12104, 12756, 6792, 142984, 120536, 51118, 49528]
    diameter = [((i / 12756) * 2) for i in diameter_km]
    distance_from_sun = [0.0, 57.9, 108.2, 149.6, 228.0, 778.5, 1432.0, 2867.0, 4515.0]

    # Create spheres for the Sun and planets
    trace0=spheres(diameter[0], '#ffff00', distance_from_sun[0]) # Sun
    trace1=spheres(diameter[1], '#87877d', distance_from_sun[1]) # Mercury
    trace2=spheres(diameter[2], '#d23100', distance_from_sun[2]) # Venus
    trace3=spheres(diameter[3], '#325bff', distance_from_sun[3]) # Earth
    trace4=spheres(diameter[4], '#b20000', distance_from_sun[4]) # Mars
    trace5=spheres(diameter[5], '#ebebd2', distance_from_sun[5]) # Jupyter
    trace6=spheres(diameter[6], '#ebcd82', distance_from_sun[6]) # Saturn
    trace7=spheres(diameter[7], '#37ffda', distance_from_sun[7]) # Uranus
    trace8=spheres(diameter[8], '#2500ab', distance_from_sun[8]) # Neptune

    # Set up orbit traces
    trace11 = orbits(distance_from_sun[1]) # Mercury
    trace12 = orbits(distance_from_sun[2]) # Venus
    trace13 = orbits(distance_from_sun[3]) # Earth
    trace14 = orbits(distance_from_sun[4]) # Mars
    trace15 = orbits(distance_from_sun[5]) # Jupyter
    trace16 = orbits(distance_from_sun[6]) # Saturn
    trace17 = orbits(distance_from_sun[7]) # Uranus
    trace18 = orbits(distance_from_sun[8]) # Neptune

    # Use the same to draw a few rings for Saturn
    trace21 = orbits(23, distance_from_sun[6], '#827962', 3) 
    trace22 = orbits(24, distance_from_sun[6], '#827962', 3) 
    trace23 = orbits(25, distance_from_sun[6], '#827962', 3)
    trace24 = orbits(26, distance_from_sun[6], '#827962', 3) 
    trace25 = orbits(27, distance_from_sun[6], '#827962', 3) 
    trace26 = orbits(28, distance_from_sun[6], '#827962', 3)

    layout=go.Layout(title = 'Le Système Solaire', showlegend=False, margin=dict(l=0, r=0, t=0, b=0),
                    #paper_bgcolor = 'black',
                    scene = dict(xaxis=dict(title='Distance du Soleil (10 puissance 6 km)', 
                                            titlefont_color='white', 
                                            range=[-7000,7000], 
                                            backgroundcolor='black',
                                            color='white',
                                            gridcolor='black'),
                                yaxis=dict(title='Distance du Soleil (10 puissance 6 km)',
                                            titlefont_color='white',
                                            range=[-7000,7000],
                                            backgroundcolor='black',
                                            color='white',
                                            gridcolor='black'
                                            ),
                                zaxis=dict(title='', 
                                            range=[-7000,7000],
                                            backgroundcolor='black',
                                            color='white', 
                                            gridcolor='black'
                                            ),
                                annotations=[
                                    annot(distance_from_sun[0], 40, 'Soleil (1,392,700km de diamètre)', xancr='left'),
                                    annot(distance_from_sun[1], 5, 'Mercure'),
                                    annot(distance_from_sun[2], 9, 'Vénus'),
                                    annot(distance_from_sun[3], 9, 'Terre'),
                                    annot(distance_from_sun[4], 7, 'Mars'),
                                    annot(distance_from_sun[5], 30, 'Jupiter'),
                                    annot(distance_from_sun[6], 28, 'Saturne'),
                                    annot(distance_from_sun[7], 20, 'Uranus'),
                                    annot(distance_from_sun[8], 20, 'Neptune'),
                                    ]
                                ))

    st.plotly_chart(go.Figure(data = [trace0, trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8,
                            trace11, trace12, trace13, trace14, trace15, trace16, trace17, trace18,
                            trace21, trace22, trace23, trace24, trace25, trace26],
                    layout = layout))


    path = ".streamlit/config.toml"
    file = open(path, "r") # Lecture 
    lines = file.readlines()
    file.close()
            
    mode = str(lines[1])

    text = ""
    if "light" in mode:
        st.warning("La visibilité est meilleure en Mode sombre")
        text = "Mode sombre"
    elif "dark" in mode:
        text = "Mode clair"

    if st.button(text):

        # Lecture du la ligne du mode du theme
        print(mode)
        
        if "dark" in  mode:
            lines[1] = mode.replace("dark", "light")
        elif "light" in mode :
            lines[1] = mode.replace("light", "dark")
        file = open(path, 'w') # Ecriture
        file.writelines(lines)
        file.close()
        
        redirect("/conclusion", True)

    video3 = open("to-scale-the-solar-system-srt-low-git_woYKwzFf.mp4", "rb")
    st.video(video3)

    st.markdown("""

    Voici un court-métrage documentaire Américain assez édifiant sur la représentation à l'échelle des planètes de notre système solaire.

    Synopsis : 
    Sur le lit d'un lac asséché du Nevada, un groupe d'amis construit la première maquette du système solaire avec les orbites complètes des planètes ; une véritable illustration de notre place dans l'univers.

    Un film de Wylie Overstreet et Alex Gorosh

    Source : "https://www.youtube.com/watch?v=zR3Igc3Rhfg&ab_channel=ToScale%3A"
    Copyright © 2015

    alexgorosh.com
    wylieoverstreet.com

    """)

    st.markdown("""

    Voici des chaînes YouTube intéressantes pour compléter la visualisation :

    https://www.youtube.com/@astrumspace/videos

    https://www.youtube.com/@REDSIDEofficial/videos

    """)

