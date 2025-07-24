import streamlit as st

# Title and description
st.set_page_config(page_title="Cas d'Entreprise – Analyse Bancaire", layout="wide")

st.title("📊 Cas d'Entreprise – Analyse Bancaire")
st.markdown("""
Bienvenue dans ce projet d'analyse bancaire. Vous trouverez ci-dessous un fichier Excel à télécharger,
contenant des données clients, agences et conseillers.

---

### 🎯 **Objectif final** :
Construire un **tableau de bord Power BI** interactif à partir des données fournies, en suivant deux business cases réalistes.

""")

# File download
with open("Data_Bankable.xlsx", "rb") as file:
    st.download_button(
        label="📥 Télécharger le fichier Excel",
        data=file,
        file_name="Banque_Entreprise_Data.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

st.markdown("---")

# =====================
# BUSINESS CASE 1
# =====================

st.header("📌 Business Case 1 : Segmentation des clients")

st.markdown("""
#### 🎯 Objectif
Aider la banque à **segmenter ses clients** pour identifier les profils les plus rentables et proposer des offres adaptées.

#### ❓ Problématique
> *Quels profils de clients (secteur, forme juridique, taille, localisation) génèrent le plus d’épargne et de patrimoine tout en présentant un risque faible (peu de découvert) ?*

#### 🧩 Données à utiliser
- `CLIENT` : données financières et RH  
- `TYPE_CLIENT` : structure juridique  
- `SECTEUR_ACTIVITE` : secteur d’activité  
- `ADRESSE`, `DEPARTEMENT`, `PAYS` : localisation

#### 🔧 Étapes détaillées

**1. Jointures nécessaires :**
- `CLIENT` → `TYPE_CLIENT` → `Libelle_Type_Client`
- `CLIENT` → `SECTEUR_ACTIVITE` → `Libelle_Secteur_Activite`
- `CLIENT` → `ADRESSE` → `DEPARTEMENT` → `PAYS` → `Ville`, `Département`, `Pays`

**2. Création d’indicateurs :**
- `Ancienneté (années)` = Année actuelle - Année d’ouverture du 1er compte  
- `Taux_Epargne` = Montant_Epargne / Montant_Total_Compte  
- `Taux_Decouvert` = Montant_Decouvert / Montant_Compte_Courant  
- `Rentabilité estimée` = Montant_Patrimoine + Montant_Total_Compte - Montant_Decouvert

**3. Analyses à produire :**
- Moyenne de rentabilité par :
  - `Secteur d’activité`
  - `Type de client`
  - `Taille d’entreprise` :  
    - 0–10, 11–50, 51–250, >250 salariés
  - `Zone géographique` (Département ou Pays)
- Histogramme de `Taux_Epargne`
- Répartition des clients de plus de 10 ans d’ancienneté

**4. Question de synthèse :**
- Quels segments seraient prioritaires pour une offre premium ?
- Quel est le **profil type** du client haute rentabilité ?

#### 📈 Tâche finale Power BI
Créer un **dashboard** avec :
- Filtres par secteur, type, taille, pays
- KPI : rentabilité, épargne, ancienneté
- Classement des **10 clients les plus rentables**

---
""")

# =====================
# BUSINESS CASE 2
# =====================

st.header("📌 Business Case 2 : Analyse de performance des agences et conseillers")

st.markdown("""
#### 🎯 Objectif
Évaluer la **performance des conseillers et agences** via leurs portefeuilles clients.

#### ❓ Problématique
> *Quels conseillers et agences gèrent les portefeuilles les plus solides en volume, ancienneté et diversité ?*

#### 🧩 Données à utiliser
- `CLIENT`  
- `SALARIE` (conseiller client)  
- `AGENCE`, `ADRESSE_AGENCE`, `DEPARTEMENT_AGENCE`, `PAYS_AGENCE`

#### 🔧 Étapes détaillées

**1. Jointures nécessaires :**
- `CLIENT` → `SALARIE` → `Nom_Salarie`
- `SALARIE` → `AGENCE` → `Nom_Agence`
- `AGENCE` → `ADRESSE_AGENCE` → `DEPARTEMENT_AGENCE` → `PAYS_AGENCE` → `Ville`, `Département`, `Pays`

**2. Création d’indicateurs :**
- `Ancienneté moyenne` des clients
- `Encours total` = somme des `Montant_Total_Compte`
- `Diversité` = nombre moyen de comptes par client
- `Ratio Découvert` = Total Découvert / Total Comptes Courants
- `Ratio Épargne` = Total Épargne / Total Comptes
- `Nombre de clients` par agence

**3. Analyses à produire :**
- Top 5 conseillers (encours/client)
- Top 5 agences (encours total)
- Carte des agences par encours
- Histogramme du ratio découvert par agence
- Classement des agences selon rentabilité moyenne

**4. Questions de synthèse :**
- Faut-il redistribuer les portefeuilles ?
- Quelles agences doivent être renforcées ?

#### 📈 Tâche finale Power BI
Créer un **dashboard** avec :
- Carte géographique des agences colorées par performance
- Filtres : agence, conseiller, département, pays
- KPIs dynamiques : encours, patrimoine, ratios
- Liste triée des clients par patrimoine

---
""")
