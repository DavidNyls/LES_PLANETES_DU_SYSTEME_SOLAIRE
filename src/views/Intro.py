import streamlit as st
import pandas as pd

st.markdown("""

# Les Planètes du Système Solaire

## Jeu de données :

""")

df = pd.read_csv(r"src\assets\planets.csv")
df

st.markdown("""

**Planet**, nom de la planète

**Color**, couleur(s) de la planète

**Mass (10^24kg)**, (chiffre dans la colonne) multiplié par 10 puissance 24 kilogrammes

**Diameter (km)**, diamètre de la planète en kilomètres

**Density (kg/m^3)**, masse volumique en kilogrammes par mètre cube

**Surface Gravity(m/s^2)**, attraction gravitationnelle en mètres par seconde au carré

**Escape Velocity (km/s)**, vitesse d'échappement :
vitesse minimale que doit atteindre un projectile pour échapper définitivement à l'attraction gravitationnelle d'une planète.
 La vitesse de libération à la surface de la Terre est de 11km/s

**Rotation Period (hours)**, durée que met la planète pour accomplir un tour sur elle-même au cours de sa rotation

**Length of Day (hours)**, durée du jour sur la planète

**Distance from Sun (10^6 km)**, (chiffre dans la colonne)x10**6kilomètres

**Perihelion (10^6 km)**, point par lequel la planète est la plus proche du Soleil

**Aphelion (10^6 km)**, point par lequel la planète est la plus éloignée du Soleil

**Orbital Period (days)**, période de révolution,
 durée mise par une planète pour accomplir une révolution complète autour du Soleil

**Orbital Velocity (km/s)**, vitesse nécessaire pour atteindre l'équilibre
 entre l'attraction de la gravité sur le satellite et l'inertie du mouvement du satellite
 la tendance du satellite à continuer à avancer

**Orbital Inclination (degrees)**, l'inclinaison de l'orbite d'une planète
 est définie comme l'angle entre le plan de l'orbite de la planète et l'écliptique.
 L'inclinaison de la Terre est donc, par définition, nulle

**Orbital Eccentricity**, l'excentricité orbitale d'un objet astronomique est un paramètre sans dimension
 qui détermine la mesure dans laquelle son orbite autour d'un autre corps s'écarte d'un cercle parfait.
 Une valeur de 0 correspond à une orbite circulaire,
 des valeurs comprises entre 0 et 1 forment une orbite elliptique,
 1 correspond à une orbite d'échappement parabolique (ou orbite de capture),
 et une valeur supérieure à 1 correspond à une hyperbole

**Obliquity to Orbit (degrees)**, le degré d'inclinaison d'une planète 
 (déterminant la répartition des saisons au cours de sa rotation pour l'exemple de la Terre)

**Mean Temperature (C)**, température moyenne sur la planète en degrés Celsius

**Surface Pressure (bars)**, pression atmosphérique, unité de pression en "bar" (exactement égale à 100 000 pascals)

**Number of Moons**, nombre de lunes/ satellites affiliés à la planète

**Ring System?**, yes or no. Est-ce que la planète possède un anneau planétaire ?

**Global Magnetic Field?**, yes or no. Est-ce que la planète possède un champ magnétique ?

""")