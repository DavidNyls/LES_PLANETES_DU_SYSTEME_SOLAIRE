# LES_PLANETES_DU_SYSTEME_SOLAIRE
French app about solar system and its planets

## Introduction

Bienvenue dans l'application de visualisation des données du système solaire. Cette application est conçue pour fournir une vue détaillée et interactive des planètes du système solaire. L'application est construite en Python, avec une architecture MVC (Modèle-Vue-Contrôleur), et comprend des visualisations de données, des vidéos, des photos et des tableaux d'analyse de données. Les visualisations sont construites en utilisant seaborn, pandas, numpy, plotly et matplotlib, tandis que les données sont stockées dans une base de données SQL et Sqlite3. L'application est déployée via Streamlit.

## Pour commencer

### Conditions préalables
Pour exécuter cette application localement, vous aurez besoin d'installer les modules suivants :

1. Python 3.7 ou dernière version
2. La bibliothèque Streamlit
3. Sqlite3
4. Seaborn
5. Matplotlib
6. Pandas
7. Numpy

Vous pouvez les installer avec les commandes suivantes :
"pip install python
pip install streamlit
pip install sqlite3
pip install seaborn
pip install matplotlib
..."

Localement les installations nécessaires se présentent comme ceci dans les différentes vues de l'architecture : 
"import streamlit as st
from src.router import redirect
import streamlit as st
import pandas as pd
import sqlite3 as sqlite
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.axes.Axes.pie
matplotlib.pyplot.pie
matplotlib.axes.Axes.legend
matplotlib.pyplot.legend
import plotly.express as px
import plotly.graph_objects as go
import math
from PIL import Image"

### Installation
1. Cloner le "repository" :
git clone https://github.com/DavidNyls/LES_PLANETES_DU_SYSTEME_SOLAIRE.git

2. Installer les packages :
Naviguer jusqu'au répertoire du projet et exécuter :
pip install -r requirements.txt
Ceci installera tout les modules nécessaires, tels que listés dans le fichier "requirements.txt" soit :
"matplotlib==3.6.2
numpy==1.23.4
pandas==1.5.1
Pillow==9.3.0
plotly==5.11.0
seaborn==0.12.1
streamlit==1.15.2"

### Lancement de l'application
Vous pouvez lancer l'application en entrant la commande suivante :
streamlit run main.py
Après avoir exécuté la commande, Streamlit fournira une URL vers votre serveur local, que vous pourrez ouvrir dans votre navigateur web pour interagir avec l'application.

## Utilisation et navigation
L'application suit une architecture MVC, ce qui signifie :

- Modèle : Représente la couche d'interaction avec la base de données où vous pouvez stocker, mettre à jour et récupérer des données.
- Vue : Représente la visualisation des données, c'est-à-dire l'interface utilisateur. C'est ici que vous pouvez voir les données dans des tableaux, des graphiques, etc.
- Contrôleur : Il sert d'interface entre le modèle et la vue pour traiter toute la logique commerciale et les demandes entrantes.
L'interface utilisateur est intuitive et facile à parcourir. Vous trouverez plusieurs sections consacrées aux différentes planètes de notre système solaire, avec des visualisations de données, des vidéos et des photos.

## Contribution
Les contributions sont ce qui fait de la communauté open-source un lieu d'apprentissage, d'inspiration et de création si extraordinaire. Toutes vos contributions sont très appréciées.

- Bifurquer vers le projet
- Créez votre branche (git checkout -b feature/AmazingFeature)
- "Commitez" vos modifications (git commit -m '...')
- "Push" vers la branche (git push origin...)
- Ouvrir une demande d'extraction (Pull)
- 
## Licence
Distribué sous la licence MIT. Voir "LICENSE" pour plus d'informations.

## Contact
David Nyls - david.nyls1@gmail.com

Lien du projet : https://github.com/DavidNyls/LES_PLANETES_DU_SYSTEME_SOLAIRE.git

Merci d'avoir consulté cette application !
