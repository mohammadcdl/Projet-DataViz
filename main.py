import streamlit as st
import pandas as pd
import plotly.express as px


data = pd.read_csv('https://data.education.gouv.fr/explore/dataset/fr-en-ips_colleges/download?format=csv&timezone=Europe/Berlin&use_labels_for_header=false', delimiter=';')

st.image("LOGO_EFREI_WEB_bleu.png", width=200)

st.markdown("""
    <div style="font-size: 28px; font-weight: bold;">🔍 Exploration de l'Indice de Position Sociale (IPS) dans les écoles françaises 🏫</div>
""", unsafe_allow_html=True)

st.write("")

st.write("""🧠 L'IPS (Indice de Position Sociale) des élèves est compris entre 38 et 179.
Plus cet indice est élevé, plus le contexte familial de l'élève est favorable à sa réussite scolaire.""")

st.markdown("""
    <div style="font-size: 20px; margin-top: 5px;"><strong>Par Mohammad DARMSY LADHA</strong></div>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="font-size: 18px; margin-top: 5px;">#dataviz2023efrei</div>
""", unsafe_allow_html=True)

st.write("")

st.write("🤔 Saviez-vous que le contexte socio-économique peut influencer la réussite scolaire d'un élève?")
st.write("Plongeons dans une analyse visuelle pour mieux comprendre ! 🚀")

# 1. Evolution de l'IPS au fil des années
st.title("1️⃣ Evolution annuelle de l'IPS 📈")
st.write("🎯 Objectif : Observer comment l'IPS moyen évolue au fil des années.")
evolution_annuelle = data.groupby('rentree_scolaire')['ips'].mean()
st.line_chart(evolution_annuelle)

st.write("📌 L'IPS semble croître au fil des années. Mais qu'en est-il lorsque nous le décomposons par région ou type d'établissement?")

# 2. Evolution de l'IPS en fonction de l'académie
st.title("2️⃣ IPS par académie 🌍")
st.write("🎯 Objectif : Comparer les tendances de l'IPS entre différentes académies.")
donnees_academie = data.groupby(['rentree_scolaire', 'academie'])['ips'].mean().unstack()
academies_choisies = donnees_academie.columns
fig = px.line(donnees_academie, x=donnees_academie.index, y=academies_choisies, labels={'value': 'IPS', 'variable': 'Académie', 'index': 'Rentrée Scolaire'})
st.plotly_chart(fig)

st.write("🧠 Les académies semblent avoir des niveaux d'IPS très différents. Cela pourrait suggérer que certaines régions ont des conditions socio-économiques plus favorables pour les élèves que d'autres. Si vous êtes curieux de savoir comment votre académie se compare, n'hésitez pas à consulter la légende afin de pouvoir compare vôtre acaadémie aux autres!")

# 3. Comparison de l'IPS entre les écoles publiques et privées
st.title("3️⃣ Public vs Privé 🏢")
st.write("🎯 Objectif : Examiner les différences d'IPS entre les établissements publics et privés.")
donnees_type = data.groupby(['rentree_scolaire', 'secteur'])['ips'].mean().unstack()
st.line_chart(donnees_type)

st.write("🧠 La distinction entre les écoles publiques et Il semble y " "avoir des différences dans le contexte socio-économique des élèves entre ces deux " "types d'établissements.")
st.write("")
st.write("Cela est compréhensible car les établissement privé ont" "généralement des ressources supplémentaires, peuvent facturer des frais de scolarité " "ou d'autres frais, et peuvent avoir la capacité de sélectionner leurs étudiants ou leur clientèle.")
st.write("")
st.write("Ces facteurs peuvent contribuer à un IPS plus élevé par rapport aux établissements publics qui sont " "financés par des fonds publics et qui, dans de nombreux cas, sont tenus de servir tous les étudiants," " quelle que soit leur position sociale. " )

# 4. Distribution de l'IPS en fonction du département
st.title("4️⃣ Distribution de l'IPS par département 📊")
st.write("🎯 Objectif : Visualiser la répartition moyenne de l'IPS par département.")
ips_departement = data.groupby('departement')['ips'].mean()
fig = px.bar(ips_departement, x=ips_departement.index, y=ips_departement.values, labels={'x': 'Département', 'y': 'IPS moyen'})
st.plotly_chart(fig)

st.write("🧠 Certains départements se démarquent par un IPS élevé, tandis que d'autres ont un IPS plus bas. Cela nous montre que chaque département à ses propres défis et opportunités. Si vous êtes de Paris, par exemple, comment pensez-vous que votre département se compare ?")

# 5. Comparaison de l'IPS pour entre les outre-mers et les autres régions en France
st.title("5️⃣ Outre-Mer vs Autres régions 🌴")
st.write("🎯 Objectif : Contraster l'IPS des régions d'Outre-Mer avec les autres régions.")
regions_outremer = ['GUADELOUPE', 'MARTINIQUE', 'GUYANE', 'LA REUNION', 'MAYOTTE']
data['region'] = data['academie'].apply(lambda x: 'Outre-Mer' if x in regions_outremer else 'Autres régions')
ips_regions = data.groupby(['rentree_scolaire', 'region'])['ips'].mean().unstack()
fig = px.line(ips_regions, x=ips_regions.index, y=['Outre-Mer', 'Autres régions'], labels={'value': 'IPS', 'variable': 'Région', 'index': 'Rentrée Scolaire'})
st.plotly_chart(fig)

st.write("🧠 Les régions d'Outre-Mer et les autres régions montrent des tendances différentes " "en matière d 'IPS. Peut-être que les différences géographiques, culturelles ou économiques " "jouent un rôle ici. C'est fascinant de voir comment la géographie peut influencer l'éducation.")
st.write("")
st.write(" La France métropolitaine semble maintenir un niveau de performance ou de situation " "stable, tandis que l'Outre-mer, bien qu'aussi stable, se trouve à un niveau nettement " "inférieur. Cela est représentatif des conditions de vie des élèves en Outre mer qui sont " "souvent difficiles comparés à la moyenne nationale.")

# 6. Comparaison de l'IPS entre les écoles publiques sur Paris et celles en périphérie parisienne
st.title("6️⃣ Paris vs Périphérie 🗼")
st.write("🎯 Objectif : Comparer l'IPS des écoles publiques de Paris avec celles de la périphérie.")
donnees_publiques = data[data['secteur'] == 'public']
periph_parisienne = ['CRETEIL', 'VERSAILLES']
donnees_academie = donnees_publiques.groupby(['rentree_scolaire', 'academie'])['ips'].mean().unstack()
donnees_academie['Paris'] = donnees_academie['PARIS']
donnees_academie['Periphery'] = donnees_academie[periph_parisienne].mean(axis=1)
comparaison_paris = donnees_academie[['Paris', 'Periphery']]
fig = px.line(comparaison_paris, x=comparaison_paris.index, y=['Paris', 'Periphery'], labels={'value': 'IPS', 'variable': 'Région', 'index': 'Rentrée Scolaire'})
st.plotly_chart(fig)

st.write("🧠 Paris, la ville lumière , comparée à ses voisins ! " "Il semble y avoir des différences notables entre le cœur " "de la capitale et sa périphérie. Cela nous rappelle que même " "à proximité, les conditions socio-économiques peuvent varier considérablement.")

st.title("🤯 Qu'est-ce que cela signifie?")
st.write("""L'IPS est un indicateur puissant qui peut nous donner un aperçu des défis et des opportunités auxquels sont confrontés les élèves en fonction de leur contexte socio-économique.""")
st.write("")
st.write("""🤔 Comment pouvons-nous utiliser ces informations pour créer un environnement éducatif plus équilibré et inclusif pour tous? C'est à nous de réfléchir et d'agir.""")
