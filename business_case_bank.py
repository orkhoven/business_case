import streamlit as st

st.set_page_config(page_title="Cas d'Entreprise – Analyse Bancaire", layout="wide")

# App Title
st.title("📊 Cas d'Entreprise – Analyse Bancaire")

# Download section
st.markdown("### 📥 Téléchargement des données")
with open("Data_Bankable.xlsx", "rb") as file:
    st.download_button(
        label="📥 Télécharger le fichier Excel",
        data=file,
        file_name="Banque_Entreprise_Data.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

# Radio button to select business case
st.markdown("### ❓ Choisissez un Business Case à explorer :")
selected_case = st.radio(
    label="",
    options=["Business Case 1 : Segmentation des clients", "Business Case 2 : Performance des agences et conseillers"],
    index=0,
    horizontal=True
)

# Styling container
def pretty_block(content):
    with st.container():
        st.markdown(
            f"""
            <div style="background-color:#f9f9f9; padding: 20px; border-radius: 10px; color: #333;">
            {content}
            </div>
            """, unsafe_allow_html=True
        )

# Business Case 1 content
if "Segmentation" in selected_case:
    pretty_block("""
    ## 📌 Business Case 1 : Segmentation des clients

    ### 🎯 Objectif  
    Aider la banque à **segmenter ses clients** pour identifier les profils les plus rentables et proposer des offres adaptées.

    ### ❓ Problématique  
    > *Quels profils de clients (secteur, forme juridique, taille, localisation) génèrent le plus d’épargne et de patrimoine tout en présentant un risque faible (peu de découvert) ?*

    ### 🧩 Données à utiliser  
    - `CLIENT`  
    - `TYPE_CLIENT`  
    - `SECTEUR_ACTIVITE`  
    - `ADRESSE`, `DEPARTEMENT`, `PAYS`  

    ### 🔧 Étapes

    **1. Jointures nécessaires :**
    - `CLIENT` → `TYPE_CLIENT` → `Libelle_Type_Client`
    - `CLIENT` → `SECTEUR_ACTIVITE` → `Libelle_Secteur_Activite`
    - `CLIENT` → `ADRESSE` → `DEPARTEMENT` → `PAYS`

    **2. Indicateurs à créer :**
    - Ancienneté (années)
    - Taux d’épargne = Montant_Epargne / Montant_Total_Compte
    - Taux de découvert = Montant_Decouvert / Montant_Compte_Courant
    - Rentabilité estimée = Montant_Patrimoine + Montant_Total_Compte - Montant_Decouvert

    **3. Analyses à produire :**
    - Rentabilité moyenne par secteur, type client, taille (0–10, 11–50, 51–250, >250)
    - Répartition des taux d’épargne
    - Ancienneté client > 10 ans

    **4. Synthèse :**
    - Quels segments viser ?
    - Quel est le profil du client « premium » ?

    ### 📈 Tâche finale Power BI  
    Créez un dashboard avec :
    - Filtres : secteur, type, taille, pays  
    - KPIs : rentabilité, épargne, ancienneté  
    - Top 10 clients les plus rentables
    """)

# Business Case 2 content
if "Performance" in selected_case:
    pretty_block("""
    ## 📌 Business Case 2 : Performance des agences et conseillers

    ### 🎯 Objectif  
    Évaluer la **performance des conseillers et agences** via leurs portefeuilles clients.

    ### ❓ Problématique  
    > *Quels conseillers et agences gèrent les portefeuilles les plus solides en volume, ancienneté et diversité ?*

    ### 🧩 Données à utiliser  
    - `CLIENT`  
    - `SALARIE`  
    - `AGENCE`, `ADRESSE_AGENCE`, `DEPARTEMENT_AGENCE`, `PAYS_AGENCE`  

    ### 🔧 Étapes

    **1. Jointures nécessaires :**
    - `CLIENT` → `SALARIE` → `Nom_Salarie`
    - `SALARIE` → `AGENCE` → `Nom_Agence`
    - `AGENCE` → `ADRESSE_AGENCE` → `DEPARTEMENT_AGENCE` → `PAYS_AGENCE`

    **2. Indicateurs à créer :**
    - Ancienneté moyenne
    - Encours total
    - Diversité : Nb_Compte moyen
    - Ratio Découvert / Encours
    - Ratio Épargne / Encours
    - Nb de clients par agence

    **3. Analyses à produire :**
    - Top 5 conseillers et agences
    - Carte des agences par performance
    - Histogrammes des ratios
    - Rentabilité moyenne par agence

    **4. Synthèse :**
    - Où renforcer les effectifs ?
    - Répartition équitable des clients ?

    ### 📈 Tâche finale Power BI  
    Créez un dashboard avec :
    - Carte géographique
    - Filtres dynamiques
    - Classements et KPIs
    """)
