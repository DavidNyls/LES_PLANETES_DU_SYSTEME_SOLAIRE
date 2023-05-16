import streamlit as st
from src.router import redirect
import os
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
import matplotlib.patches as mpatches
from PIL import Image

def load_view():

    st.sidebar.header("Les planètes")
    selection = st.sidebar.selectbox("Selectionner une planète", ["Mercure", "Vénus", "Terre", "Mars", "Jupiter", "Saturne", "Uranus", "Neptune"])
    # Style the sidebar to be sticky and visible on small screens
    st.markdown(
        """
        <style>
            .sidebar .sidebar-content {
                position: -webkit-sticky !important;
                position: sticky !important;
                top: 55px !important; /* height of the navbar */
                max-height: 100vh !important;
                overflow-y: auto !important;
                -webkit-overflow-scrolling: touch !important;
            }

            @media (max-width: 767px) {
                .sidebar .sidebar-content {
                    position: fixed !important;
                    top: 0 !important;
                    left: 0 !important;
                    width: 100% !important;
                    height: 100% !important;
                    z-index: 9999 !important;
                    overflow-y: auto !important;
                    background-color: white !important;
                        }
                    }
                </style>
                """,
                unsafe_allow_html=True,
    )
    if selection == "Mercure":
        image = Image.open('./src/assets/images/Mercure_img.png')
        with st.sidebar:
            st.image(image)
            st.header("Petit Monde")
            st.markdown("Mercure est la plus petite planète de notre système solaire, elle est seulement un peu plus grande que notre Lune. Mercure est aussi la planète la plus rapide de notre système solaire à entreprendre une révolution complète autour du Soleil !")
            st.header("Planète inhospitalière")
            st.markdown("La fine atmosphère de Mercure, ou exosphère, est composée principalement d'oxygène (O2), de sodium (Na), d'hydrogène (H2), d'hélium (He) et de potassium (K). Il est peu probable que la vie telle que nous la connaissons puisse survivre sur Mercure en raison des radiations solaires et des températures extrêmes.")
            st.header("Grand Soleil")
            st.markdown("Si l'on se tenait à la surface de Mercure, notre Soleil nous apparaîtrait trois fois plus grand que sur la Terre.")

    if selection == "Vénus":
        image = Image.open('./src/assets/images/Venus_img.png')
        with st.sidebar:
            st.image(image)
            st.header("Jumelle Toxique !")
            st.markdown("Vénus est souvent appelée 'la jumelle de la Terre' car elles sont similaires en taille et en structure, mais Vénus a une chaleur de surface extrême et une atmosphère dense et toxique. Si le Soleil était aussi haut qu'une porte d'entrée typique, la Terre et Vénus auraient chacune la taille d'une pièce de 5 cents.")
            st.header("Années courtes, journées longues")
            st.markdown("Vénus tourne très lentement sur son axe - un jour sur Vénus dure 243 jours terrestres. Cependant, la planète tourne autour du Soleil plus rapidement que la Terre, de sorte qu'une année sur Vénus ne dure qu'environ 225 jours terrestres, ce qui fait qu'un jour vénusien est plus long que son année !")
            st.header("Rotation inverse")
            st.markdown("Vénus tourne à l'envers sur son axe par rapport à la plupart des planètes de notre système solaire. Cela signifie que le Soleil se lève à l'ouest et se couche à l'est, à l'opposé de ce que nous voyons sur Terre.")



    if selection == "Terre":
        image = Image.open('./src/assets/images/Terre_img.png')
        with st.sidebar:
            st.image(image)
            st.header("Home Sweet Home")
            st.markdown("La Terre est l'endroit parfait pour la vie telle que nous la connaissons. L'atmosphère terrestre est composée de 78 pourcents d'azote, de 21 pourcents d'oxygène et de 1 pourcent d'autres ingrédients - l'équilibre parfait pour respirer et vivre.")
            st.header("Bouclier protecteur")
            st.markdown("Notre atmosphère nous protège des météoroïdes, dont la plupart se brisent dans l'atmosphère avant d'en toucher la surface.")
            st.header("La 3e Terrestre")
            st.markdown("La Terre est la troisième planète la plus proche du Soleil, à une distance d'environ 150 millions de km (93 millions de miles). Une journée sur Terre dure 24 heures. La Terre fait une orbite complète autour du soleil (une année en temps terrestre) en environ 365 jours.")


    if selection == "Mars":
        image = Image.open('./src/assets/images/Mars_img.png')
        with st.sidebar:
            st.image(image)
            st.header("Petite Planète")
            st.markdown("Si le Soleil était aussi haut qu'une porte d'entrée classique, la Terre aurait la taille d'une balle de 'ping-pong' et Mars serait à peu près aussi grande qu'un cachet d'aspirine.")
            st.header("Terrain rugueux")
            st.markdown("Mars est une planète rocheuse. Elle possède une fine atmosphère composée principalement de dioxyde de carbone (CO2), d'argon (Ar), d'azote (N2) et d'une petite quantité d'oxygène et de vapeur d'eau.")
            st.header("Deux Lunes")
            st.markdown("Mars a deux lunes nommées Phobos et Deimos.")
            st.header("Plusieurs explorations")
            st.markdown("Plusieurs missions ont visité cette planète, depuis les survols et les orbiteurs jusqu'aux rovers à la surface. Le premier véritable succès d'une mission sur Mars a été le survol de Mariner 4 en 1965.")

    if selection == "Jupiter":
        image = Image.open('./src/assets/images/Jupiter_img.png')
        with st.sidebar:
            st.image(image)
            st.header("La plus Grande Planète")
            st.markdown("Si la Terre avait la taille d'un raisin, Jupiter aurait la taille d'un ballon de basket.")
            st.header("Journées courtes/ années longues")
            st.markdown("Jupiter effectue une rotation toutes les 10 heures environ, mais met environ 12 années terrestres pour effectuer une orbite autour du Soleil.")
            st.header("Que s'y cache-t-il ?")
            st.markdown("Jupiter est une géante gazeuse et n'a donc pas une surface semblable à celle de la Terre. Si elle possède un noyau interne solide, il est probablement de la taille de la Terre. La grande tache rouge de Jupiter est une tempête gigantesque qui fait environ deux fois la taille de la Terre et qui fait rage depuis plus d'un siècle.")
            st.header("Anneau invisible")
            st.markdown("En 1979, la sonde Voyager a découvert le discret système d'anneaux de Jupiter. Les 4 géantes en sont donc pourvus.")
            st.header("Des traces de vie possibles ?")
            st.markdown("Jupiter ne peut pas supporter la vie telle que nous la connaissons. Mais certaines des 79 lunes de Jupiter ont des océans sous leur croûte qui pourraient abriter la vie.")




    if selection == "Saturne":
        image = Image.open('./src/assets/images/Saturn_img.png')
        with st.sidebar:
            st.image(image)
            st.header("Air Chaud")
            st.markdown("Comme Jupiter, l'atmosphère de Saturne est essentiellement constituée d'hydrogène et d'hélium")
            st.header("Les célèbres anneaux")
            st.markdown("Saturne possède le système d'anneaux le plus spectaculaire, avec sept anneaux et plusieurs lacunes et divisions entre eux.")
            st.header("De Nombreuses Lunes")
            st.markdown("Saturne compte 53 lunes connues et 29 autres attendent la confirmation de leur découverte, soit un total de 82 lunes.")
            st.header("Expérience Terrestre")
            st.markdown("Environ deux tonnes de la masse de Saturne proviennent de la Terre : le vaisseau spatial Cassini a été intentionnellement vaporisé dans l'atmosphère de Saturne en 2017.")

    if selection == "Uranus":
        image = Image.open('./src/assets/images/Uranus_img.png')
        with st.sidebar:
            st.image(image)
            st.header("Jour court/ année longue")
            st.markdown("Uranus met environ 17 heures pour effectuer une rotation (un jour uranien) et environ 84 années terrestres pour effectuer une orbite autour du Soleil (une année uranienne).")
            st.header("Géante de Glace")
            st.markdown("Uranus est une géante de glace. La majeure partie de sa masse est constituée d'un fluide chaud et dense de matériaux 'glacés' - eau, méthane et ammoniac - au-dessus d'un petit noyau rocheux.")
            st.header("Rotation")
            st.markdown("Comme Vénus, Uranus tourne d'est en ouest. Mais Uranus est unique en ce qu'elle tourne sur le côté.")
            st.header("Les anneaux d'Uranus")
            st.markdown("Uranus possède 13 anneaux connus. Les anneaux intérieurs sont étroits et sombres et les anneaux extérieurs sont de couleur vive.")

    if selection == "Neptune":
        image = Image.open('./src/assets/images/Neptune_img.png')
        with st.sidebar:
            st.image(image)
            st.header("Géante Glacée 2")
            st.markdown("Neptune est une géante de glace. La majeure partie de sa masse est constituée d'un fluide chaud et dense de matériaux 'glacés' - eau, méthane et ammoniac - au-dessus d'un petit noyau rocheux.")
            st.header("Lunes")
            st.markdown("Neptune possède 14 lunes connues qui portent le nom de dieux et de nymphes de la mer dans la mythologie grecque.")
            st.header("Un seul voyage")
            st.markdown("Voyager 2 est le seul vaisseau spatial à avoir visité Neptune. Aucun vaisseau spatial n'a tourné autour de cette planète lointaine pour l'étudier en détail et de près.")
            st.header("les anneaux de Neptune")
            st.markdown("Neptune possède au moins cinq anneaux principaux et quatre autres arcs d'anneaux, qui sont des amas de poussière et de débris probablement formés par la gravité d'une lune proche.")


    df = pd.read_csv("./src/assets/planets.csv")
    st.dataframe(df)

    video1 = open("main-bg-low-git_g5YQ2dCq.mp4", "rb")
    st.video(video1)

    ndf = pd.DataFrame({"Planètes": ["Mercure", "Vénus", "Terre", "Mars", "Jupiter", "Saturne", "Uranus", "Neptune"],
    "Type de planète:" : ["Terrestre", "Terrestre", "Terrestre", "Terrestre", "Gazeuse", "Gazeuse", "Gazeuse", "Gazeuse"],
    "Masse (10 puissance 24kg)": [0.33, 4.87, 5.97, 0.642, 1898, 568, 86.8, 102],
    "Diameter (km)": [4879, 12104, 12756, 6792, 142984, 120536, 51118, 49528]})

    st.markdown("""
    
    ### Envergure et Masse de Jupiter
    
    """)

    st.plotly_chart(px.scatter(ndf, x="Planètes", y="Masse (10 puissance 24kg)", size="Diameter (km)", color="Type de planète:"))

    st.markdown("""
    
    Jupiter est un peu moins de 318 fois plus massive que la Terre. Cette géante fait près de 11 fois la taille de la Terre. Si l'on pouvait marcher pour en faire le tour (chose impossible car Jupiter est une planète gazeuse) au rythme soutenu de 40km par jour, ce voyage nous prendrait 33 ans environ !

    """)

    xdf = pd.DataFrame({"Planètes": ["Mercure", "Vénus", "Terre", "Mars", "Jupiter", "Saturne", "Uranus", "Neptune"],
    "Distance du Soleil (10 puissance 6 km)": [57.9, 108.2, 149.6, 228.0, 778.5, 1432.0, 2867.0, 4515.0],
    "Densité (kg/m³)": [5429, 5243, 5514, 3934, 1326, 687, 1270, 1638]})
    
    st.markdown("""
    
    ### Densité et distance de Saturne
    
    """)

    st.plotly_chart(px.scatter(xdf, x = "Distance du Soleil (10 puissance 6 km)", 
    y = "Densité (kg/m³)", size = "Densité (kg/m³)", color = "Planètes"))

    st.markdown("""
    
    La Terre est la planète la plus dense du système solaire, tandis que Saturne est la moins dense. La densité de la Terre est de 5,52 g/cm3, tandis que celle de Saturne est de 0,687 g/cm3. En d'autres termes, la Terre est 8 fois plus dense que Saturne. Saturne est la seule planète dont la densité est inférieure à celle de l'eau. Autrement dit, si l'on trouvait une baignoire assez grande pour y mettre la planète, elle y flotterait ! 1,2 à 1,7 milliard de kilomètres séparent la Terre de Saturne selon leur position orbitale.

    """)

    zdf = pd.DataFrame({"Planet": ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"],
    "Atmosphère principale" : ["Aucune", "dioxyde de carbone", "diazote", "dioxyde de carbone", "hydrogène/hélium", "hydrogène/hélium", "hydrogène/hélium", "hydrogène/hélium"],
    "Distance du Soleil (10 puissance 6 km)": [57.9, 108.2, 149.6, 228.0, 778.5, 1432.0, 2867.0, 4515.0],
    "Vitesse d'évasion (en km/s)": [4.3, 10.4, 11.2, 5.0, 59.5, 35.5, 21.3, 23.5],
    "Température moyenne": [440.15, 737.15, 288.15, 208.15, 163.15, 133.15, 78.15, 73.15]})
    
    st.markdown("""
    
    ### Composition atmosphérique principale des Planètes
    
    """)

    st.plotly_chart(px.scatter(zdf, x="Vitesse d'évasion (en km/s)", y="Distance du Soleil (10 puissance 6 km)", 
    size='Température moyenne', color='Atmosphère principale'))

    st.markdown("""
    
    Jupiter a une vitesse d'évasion de 59,5 km/s. Si l'on compare cette vitesse à celle de la Terre, la vitesse d'évasion est cinq fois plus élevée pour échapper à l'attraction gravitationnelle de Jupiter. C'est pourquoi l'atmosphère de Jupiter est principalement constituée d'hydrogène et d'hélium. Ces gaz n'ont pas pu s'échapper depuis la formation de Jupiter à cause de sa vitesse d'échappement.

    """)

    adf = pd.DataFrame({"Planètes": ["Mercure", "Vénus", "Terre", "Mars", "Jupiter", "Saturne", "Uranus", "Neptune"],
    "intensité champ gravitationnel (m/s²)": [3.7, 8.9, 9.8, 3.7, 23.1, 9.0, 8.7, 11.0]})
    
    st.markdown("""
    
    ### Champ gravitationnel de Jupiter
    
    """)
    st.bar_chart(adf, x="Planètes", y="intensité champ gravitationnel (m/s²)")

    st.markdown("""
    
    Jupiter possède un champ magnétique, 14 fois plus puissant que celui de la Terre, allant de 4,2 G à l'équateur à 10 à 14 G aux pôles, ce qui en fait le plus intense du Système solaire. Si vous pesez 65 kg sur terre, vous n'en feriez que 58 kg sur Vénus et 24.51 kg sur Mars (pour seulement 10.7 kg sur la Lune) mais 153 kg sur Jupiter,  dont la gravité est 2,5 plus forte que celle de la Terre.

    """)

    bdf = pd.DataFrame({"Planètes": ["Mercure", "Vénus", "Terre", "Mars", "Jupiter", "Saturne", "Uranus", "Neptune"],
    "Période de rotation (heures)": [1407.6, -5832.5, 23.9, 24.6, 9.9, 10.7, -17.2, 16.1]})
    
    st.markdown("""
    
    ### Rotation de Vénus
    
    """)

    fig = plt.figure()
    ax = sns.barplot(data=bdf, x="Planètes", y="Période de rotation (heures)")
    ax.set(yscale = "symlog")
    st.pyplot(fig)

    st.markdown("""
    
    Vénus effectue une rotation inverse au sens des aiguilles d'une montre tous les 243 jours terrestres - la rotation la plus lente de toutes les planètes. Cette rotation rétrograde, est à l’origine des jours solaires plus courts (58 jours et 9 heures) que le jour sidéral (116 jours et 18 heures).  A l'inverse, la Terre a un jour solaire moyen de 24h et un jour sidéral de 23h 56min 4,09s.

    """)

    cdf = pd.DataFrame({"Planètes": ["Mercure", "Vénus", "Terre", "Mars", "Jupiter", "Saturne", "Uranus", "Neptune"],
    "Durée du jour (heures)": [4222.6, 2802.0, 24.0, 24.7, 9.9, 10.7, 17.2, 16.1]})

    st.markdown("""
    
    ### Journée mercurienne
    
    """)

    fig = plt.figure()
    bx = sns.barplot(data=cdf, x="Planètes", y="Durée du jour (heures)")
    bx.set(yscale="log")
    st.pyplot(fig)

    st.markdown("""
    
    Une année ne dure que 88 jours sur Mercure, mais grâce à sa rotation lente, un jour dure deux fois plus longtemps ! Cela signifie que si vous vous teniez à la surface de Mercure, il faudrait 176 jours terrestres pour que le Soleil se lève, se couche et se relève une seule fois au même endroit dans le ciel !

    """)

    ddf = pd.DataFrame({"Planètes": ["Mercure", "Vénus", "Terre", "Mars", "Jupiter", "Saturne", "Uranus", "Neptune"],
    "Distance du Soleil (10 puissance 6 km)": [57.9, 108.2, 149.6, 228.0, 778.5, 1432.0, 2867.0, 4515.0],
    "intensité champ gravitationnel (mètres/s au carré)": [3.7, 8.9, 9.8, 3.7, 23.1, 9.0, 8.7, 11.0],
    "Température moyenne (C°)": [167, 464, 15, -65, -110, -140, -195, -200]})

    st.markdown("""
    
    ### le Climat sur les planètes
    
    """)

    st.plotly_chart(px.scatter(ddf, x="Planètes", y="Distance du Soleil (10 puissance 6 km)", 
    size='intensité champ gravitationnel (mètres/s au carré)', color='Température moyenne (C°)', color_continuous_scale='Bluered'))

    st.markdown("""
    
    Neptune est si éloignée du Soleil que midi sur la grande planète bleue nous paraîtrait comme un faible crépuscule. La lumière chaude que nous voyons depuis notre planète est environ 900 fois plus intense que celle visible sur Neptune. La température moyenne sur Vénus est quant à elle de 462°C. La distance entre Vénus et le soleil ne joue qu'un petit rôle dans la cause de sa vague de chaleur élevée. L'atmosphère de Vénus est presque entièrement constituée de dioxyde de carbone et son contacte avec le Soleil produit un effet de serre qui intensifie la chaleur sur la planète.

    """)

    edf = df["Aphelion (10^6 km)"]- df["Perihelion (10^6 km)"] 
    pdf = pd.DataFrame({"Planètes": ["Mercure", "Vénus", "Terre", "Mars", "Jupiter", "Saturne", "Uranus", "Neptune"],
    "Périhélie (10 puissance 6 km)": [46.0, 107.5, 147.1, 206.7, 740.6, 1357.6, 2732.7, 4471.1]})

    st.markdown("""
    
    ### les Saisons et les Planètes
    
    """)

    fdf = pd.concat([pdf, edf], axis=1)
    fdf.rename(columns = {0:'Aphélie (10 puissance 6 km)'}, inplace = True)
    # fdf = fdf.set_index('Planètes')
    fig, ax = plt.subplots()
    
    fdf.plot.bar(x='Planètes',
                y = ['Périhélie (10 puissance 6 km)', 'Aphélie (10 puissance 6 km)'],
                stacked = True, ax = ax)
    st.pyplot(fig)
    

    st.markdown("""
    
    Les différences périhélie et aphélie d'Uranus sont légèrement remarquables par rapport aux autres planètes. L'aphélie d'Uranus se démarque ce qui signifie que la différence dans la quantité de chaleur et de lumière qu'elle reçoit du Soleil varie nettement plus que pour les autres planètes. Cela crée des changements saisonniers complètement différents de ceux des autres planètes. Près du solstice, un pôle fait face au Soleil en continu et l'autre est tourné vers l'extérieur. Chaque pôle obtient donc environ 42 années d'ensoleillement continu suivies d'autant d'années d'obscurité. Seule une bande étroite autour de l'équateur connaît un cycle jour-nuit rapide, mais avec le soleil très bas à l'horizon. Ceci pourrait s'expliquer par l'inclinaison axiale atypique de la planète (97,77° pour 23° sur la Terre).

    """)

    gdf = pd.DataFrame({"Planètes": ["Mercure", "Vénus", "Terre", "Mars", "Jupiter", "Saturne", "Uranus", "Neptune"],
    "Type de planète:" : ["Terrestre", "Terrestre", "Terrestre", "Terrestre", "Gazeuse", "Gazeuse", "Gazeuse", "Gazeuse"],
    "Vitesse Orbitale (km/s)": [47.4, 35.0, 29.8, 24.1, 13.1, 9.7, 6.8, 5.4],
    "Diameter (km)": [4879, 12104, 12756, 6792, 142984, 120536, 51118, 49528],
    "Période de révolution (jours)": [88.0, 224.7, 365.2, 687.0, 4331.0, 10747.0, 30589.0, 59800.0],
    "Distance du Soleil (10 puissance 6 km)": [57.9, 108.2, 149.6, 228.0, 778.5, 1432.0, 2867.0, 4515.0]})

    st.markdown("""
    
    ### Vitesse Orbitale et Période de Révolution sur Neptune
    
    """)

    st.plotly_chart(px.scatter_3d(gdf, x='Vitesse Orbitale (km/s)', y='Période de révolution (jours)', z='Distance du Soleil (10 puissance 6 km)', color='Type de planète:'))

    st.markdown("""
    
    En 2011 Neptune complète sa première orbite de 165 ans autour du soleil depuis sa découverte en 1846. En moyenne, la vitesse orbitale de Neptune est de 5.4km/s pour 29.8km/s sur la Terre. L'orbite elliptique et ovale de Neptune maintient la planète à une distance moyenne du soleil de près de 4,5 milliards de kilomètres, soit environ 30 fois la distance de la Terre, ce qui la rend invisible à l'œil nu.

    """)

    
    hdf = pd.DataFrame({"Planètes": ["Mercure", "Vénus", "Terre", "Mars", "Jupiter", "Saturne", "Uranus", "Neptune"],
    "Inclinaison Orbitale (degrés)": [7.0, 3.4, 0.0, 1.8, 1.3, 2.5, 0.8, 1.8]})

    st.markdown("""
    
    ### Inclinaison Orbitale de Mercure
    
    """)

    fig = plt.figure()
    sns.barplot(data=hdf, x="Planètes", y="Inclinaison Orbitale (degrés)")
    st.pyplot(fig)

    st.markdown("""
    
    L'inclinaison orbitale de Mercure (7 degrés) pourrait avoir empêché Vénus de créer sa propre lune. De récentes études expliquent que les planètes pourraient ne pas être totalement étrangères les unes aux autres concernant l'inclinaison de leur orbite, celles-ci seraient interconnectées. Ces théories contredisent la théorie de Newton sur la gravité de la masse du Soleil et le concept d'indépendance du mouvement des planètes (La planète Terre est le point de référence, c'est pourquoi elle est définie à 0).

    """)

    idf = pd.DataFrame({"Planètes": ["Mercure", "Vénus", "Terre", "Mars", "Jupiter", "Saturne", "Uranus", "Neptune"],
    "Excentricité Orbitale": [0.206, 0.007, 0.017, 0.094, 0.049, 0.052, 0.047, 0.01]})

    st.markdown("""
    
    ### Excentricité Orbitale de Mercure
    
    """)

    fig = plt.figure()
    sns.barplot(data=idf, x="Planètes", y="Excentricité Orbitale")
    st.pyplot(fig)

    st.markdown("""
    
    En raison de son excentricité relativement élevée (une variation de l'énergie solaire équivalente à 6 fois l'énergie solaire totale que nous recevons sur Terre), les températures moyennes de surface dépendent fortement de la latitude, mais aussi de la longitude. Mercure connaît une variation de température d'environ 100 degrés autour de l'équateur.
    """)

    jdf = pd.DataFrame({"Planètes Terrestres": ["Mercure", "Vénus", "Terre", "Mars"],
    "Inclinaison de l'axe (degrés)": [0.034, 177.4, 23.4, 25.2],
    "Diameter (km)": [4879, 12104, 12756, 6792],
    "Distance du Soleil (10 puissance 6 km)": [57.9, 108.2, 149.6, 228.0],})

    st.markdown("""
    
    ### L'Obliquité de Vénus
    
    """)

    st.plotly_chart(px.scatter_polar(jdf, r='Distance du Soleil (10 puissance 6 km)', theta="Inclinaison de l'axe (degrés)",
              color='Planètes Terrestres', size="Diameter (km)"))

    st.markdown("""
    
    Vénus s'est peut-être formée à partir de la nébuleuse solaire avec une période de rotation et une obliquité différentes, atteignant son état actuel en raison de changements chaotiques de rotation causés par des perturbations planétaires et des effets de marée sur son atmosphère dense, un changement qui se serait produit au cours de milliards d'années.
    
    """)

    video2 = open("obliq-low-res_CQstA5Jd.mp4", "rb")
    st.video(video2)

    kdf = pd.DataFrame({"Planètes": ["Mercure", "Vénus", "Terre", "Mars", "Jupiter", "Saturne", "Uranus", "Neptune"],
    "Nombre de Lunes": [0, 0, 1, 2, 79, 82, 27, 14]})

    st.markdown("""
    
    ### Les nombreux Satellites de Saturne
    
    """)

    fig = plt.figure()
    sns.barplot(data=kdf, x="Planètes", y="Nombre de Lunes")
    st.pyplot(fig)

    st.markdown("""
    
    Saturne compte officiellement 53 lunes, et 29 autres attendent actuellement que l'Union astronomique internationale confirme leur découverte et leur nom. Les satellites de Saturne sont très différents dans leur composition, allant des géants glacés avec des océans souterrains aux petits mondes rocheux fortement cratérisés qui semblent tout droit sortis d'un film de science-fiction. Sept des lunes de Saturne sont si brillantes qu'elles sont visibles de la Terre au moyen d'un télescope !
    
    """)

    fig, ax = plt.subplots(figsize=(9, 6), subplot_kw=dict(aspect="equal"))
    Periode_orbitale = ["Jupiter: 59,5 km/s",
                        "Saturne: 35,5 km/s",
                        "Uranus: 21,3 km/s",
                        "Neptune: 23,5 km/s"]

    data = [59.5, 35.5, 21.3, 23.5]

    st.markdown("""
    
    ### Les anneaux planétaires des géantes et leur vitesse d'évasion
    
    """)

    wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(Periode_orbitale[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                    horizontalalignment=horizontalalignment, **kw)


    st.pyplot(fig)

    st.markdown("""
    
    Les anneaux planétaires sont des essaims d'objets orbitant autour d'une planète centrale avec des mouvements verticaux qui sont faibles par rapport à leurs mouvements dans un plan commun. Cette caractéristique est due au fait que leurs planètes tournent assez vite pour se bomber à leurs équateurs, définissant ainsi un plan orbital privilégié. Plus les planètes sont loin du Soleil, plus leur période de révolution s'étend. Neptune met 165 années (repère terrestre) pour accomplir une révolution complète autour du Soleil, contre 1 an pour la Terre.
    
    """)

    if st.button("conclusions"):
        redirect("/conclusions", reload=True)