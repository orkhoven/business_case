#!/usr/bin/env python
# coding: utf-8



import streamlit as st

# Title and description
st.title("📊 Cas d'Entreprise – Analyse Bancaire")
st.markdown("""
Bienvenue dans ce projet d'analyse bancaire. Vous trouverez ci-dessous un fichier Excel à télécharger,
contenant des données clients, agences et conseillers.

Deux business cases vous sont proposés :  
- **Segmentation client pour offres personnalisées**
- **Analyse de performance des agences et conseillers**

**Objectif final :** Construire un tableau de bord Power BI.

---  
""")

# File download
with open("Data_Bankable.xlsx", "rb") as file:
    st.download_button(
        label="📥 Télécharger le fichier Excel",
        data=file,
        file_name="Banque_Entreprise_Data.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

# Display instructions
st.markdown("""
🎯 Objectif :
Aider la banque à segmenter ses clients pour identifier les profils les plus rentables et proposer des offres adaptées.

❓ Problématique :
"Quels profils de clients (secteur, forme juridique, taille, localisation) génèrent le plus d’épargne et de patrimoine tout en présentant un risque faible (peu de découvert) ?"

🧩 Données à utiliser :
CLIENT : données financières et RH

TYPE_CLIENT : structure juridique

SECTEUR_ACTIVITE : secteur d’activité

ADRESSE, DEPARTEMENT, PAYS : localisation du client

🔧 Étapes détaillées :
1. 🔗 Jointures nécessaires :
CLIENT → TYPE_CLIENT → ajouter Libelle_Type_Client

CLIENT → SECTEUR_ACTIVITE → ajouter Libelle_Secteur_Activite

CLIENT → ADRESSE → DEPARTEMENT → PAYS → ajouter Ville, Département, Pays

2. 📐 Création d’indicateurs :
Ancienneté (en années) = Année actuelle - Année d’ouverture du premier compte

Taux_Epargne = Montant_Epargne / Montant_Total_Compte

Taux_Decouvert = Montant_Decouvert / Montant_Compte_Courant
(attention aux divisions par zéro !)

Rentabilité estimée = Montant_Patrimoine + Montant_Total_Compte - Montant_Decouvert

3. 📊 Analyses à produire :
Moyenne de Rentabilité estimée par :

Libelle_Secteur_Activite

Libelle_Type_Client

Taille d’entreprise (Nb_Salarie en classes : 0-10, 11-50, 51-250, >250)

Localisation géographique (Département ou Pays)

Répartition par Taux_Epargne (histogramme)

Répartition des clients anciens (>10 ans) par secteur

4. 📌 Question de synthèse :
Quels segments seraient prioritaires pour une nouvelle offre premium ?

Quel est le profil type du client « haute rentabilité » ?

📈 Tâche finale Power BI :
Créer un dashboard interactif permettant :

Le filtrage par secteur, type, taille, pays

L'affichage des KPI principaux : rentabilité, épargne, ancienneté

Un classement des 10 clients les plus rentables
""")





