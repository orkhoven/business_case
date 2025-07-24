import streamlit as st

# Set up page
st.set_page_config(page_title="Analyse Bancaire", layout="wide")

# Title
st.title("Analyse Bancaire")

# --- Download section ---
st.markdown("### 📥 Téléchargement des données")
with open("Data_Bankable.xlsx", "rb") as file:
    st.download_button(
        label="📥 Télécharger le fichier Excel",
        data=file,
        file_name="Banque_Entreprise_Data.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

st.markdown("---")

# --- Case selector ---
st.markdown("### Choisissez un Business Case à explorer :")
selected_case = st.radio(
    label="",
    options=["", "Business Case 1 : Segmentation des clients", "Business Case 2 : Performance des agences et conseillers"],
    index=0,
    horizontal=True
)

# Display only if a choice is made
if selected_case:

    # --- Business Case 1 ---
    if "Segmentation" in selected_case:
        st.header("📌 Business Case 1 : Segmentation des clients")

        st.markdown("""
        ### 🎯 Objectif  
        Aider la banque à **segmenter ses clients** pour identifier les profils les plus rentables et proposer des offres adaptées.

        ### ❓ Problématique  
        Quels profils de clients (secteur, forme juridique, taille, localisation) génèrent le plus d’épargne et de patrimoine tout en présentant un risque faible (peu de découvert) ?

        ### 🧩 Données à utiliser  
        - `CLIENT` : données financières et RH  
        - `TYPE_CLIENT` : structure juridique  
        - `SECTEUR_ACTIVITE` : secteur d’activité  
        - `ADRESSE`, `DEPARTEMENT`, `PAYS` : localisation

        ### 🔧 Étapes

        **1. Jointures nécessaires :**  
        - `CLIENT` → `TYPE_CLIENT` → `Libelle_Type_Client`  
        - `CLIENT` → `SECTEUR_ACTIVITE` → `Libelle_Secteur_Activite`  
        - `CLIENT` → `ADRESSE` → `DEPARTEMENT` → `PAYS`

        **2. Indicateurs à créer (avec explication) :**

        - **Ancienneté du client**  
          > Calculée à partir de la `Date_Ouverture_1er_Compte`, cette mesure permet d’estimer la fidélité et la valeur à long terme d’un client.

        - **Taux d’épargne** = Montant_Epargne / Montant_Total_Compte  
          > Indique si le client place une part importante de son argent sur des produits d’épargne, ce qui est généralement un bon indicateur de stabilité financière.

        - **Taux de découvert** = Montant_Decouvert / Montant_Compte_Courant  
          > Permet de mesurer la part d’endettement à court terme ou les besoins en trésorerie. Un taux élevé peut signaler un risque ou une mauvaise gestion.

        - **Rentabilité estimée du client** = Montant_Patrimoine + Montant_Total_Compte - Montant_Decouvert  
          > C’est une estimation simple du potentiel économique du client pour la banque, en tenant compte de ses actifs nets.

        **3. Analyses à produire :**
        - Rentabilité moyenne par secteur, type client, taille (0–10, 11–50, 51–250, >250)
        - Répartition des taux d’épargne
        - Ancienneté client > 10 ans

        **4. Questions de synthèse :**
        - Quels segments viser ?
        - Quel est le profil du client « premium » ?

        ### 📈 Tâche finale Power BI  
        Créez un dashboard avec :
        - Filtres : secteur, type, taille, pays  
        - KPIs : rentabilité, épargne, ancienneté  
        - Top 10 clients les plus rentables
        """)

    # --- Business Case 2 ---
    elif "Performance" in selected_case:
        st.header("📌 Business Case 2 : Performance des agences et conseillers")

        st.markdown("""
        ### 🎯 Objectif  
        Évaluer la **performance des conseillers et agences** via leurs portefeuilles clients.

        ### ❓ Problématique  
        > *Quels conseillers et agences gèrent les portefeuilles les plus solides en volume, ancienneté et diversité ?*

        ### 🧩 Données à utiliser  
        - `CLIENT`  
        - `SALARIE` (conseiller client)  
        - `AGENCE`, `ADRESSE_AGENCE`, `DEPARTEMENT_AGENCE`, `PAYS_AGENCE`

        ### 🔧 Étapes

        **1. Jointures nécessaires :**  
        - `CLIENT` → `SALARIE` → `Nom_Salarie`  
        - `SALARIE` → `AGENCE` → `Nom_Agence`  
        - `AGENCE` → `ADRESSE_AGENCE` → `DEPARTEMENT_AGENCE` → `PAYS_AGENCE`

        **2. Indicateurs à créer (avec explication) :**

        - **Ancienneté moyenne des clients**  
          > Permet d’estimer la stabilité du portefeuille géré par un conseiller ou une agence. Un bon indicateur de fidélisation.

        - **Encours total**  
          > Représente le volume total géré (épargne + compte courant), c’est l’un des indicateurs les plus critiques de performance.

        - **Diversité des comptes** (`Nb_Compte` moyen par client)  
          > Plus un client possède de produits, plus il est engagé avec la banque. Cela indique aussi la capacité du conseiller à vendre plusieurs offres.

        - **Ratio Découvert / Encours**  
          > Mesure le niveau de risque associé à un portefeuille. Un ratio élevé peut indiquer une exposition plus risquée.

        - **Ratio Épargne / Encours**  
          > Indique la solidité du portefeuille : plus il y a d’épargne, plus le portefeuille est stable et peu volatile.

        - **Nombre de clients par agence**  
          > Aide à analyser la charge commerciale et à identifier les agences surchargées ou sous-utilisées.

        **3. Analyses à produire :**
        - Top 5 conseillers et agences
        - Carte des agences par performance
        - Histogrammes des ratios
        - Rentabilité moyenne par agence

        **4. Questions de synthèse :**
        - Où renforcer les effectifs ?
        - Répartition équitable des clients ?

        ### 📈 Tâche finale Power BI  
        Créez un dashboard avec :
        - Carte géographique des agences  
        - Filtres dynamiques : agence, conseiller, département, pays  
        - Classements, KPIs et ratios
        """)
