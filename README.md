# Analyseur de Sentiment YouTube

Extension Chrome et API Cloud FastAPI pour l’analyse de sentiment en temps réel des commentaires YouTube.

## Fonctionnalités

- Extraction et classification des commentaires YouTube : positif, neutre, négatif
- Extension Chrome simple : statistiques, filtrage, mode sombre
- API FastAPI déployée sur Hugging Face Spaces
- Modèle ML entraîné (TF-IDF + Régression Logistique)
- Installation rapide et projet facilement reproductible

## Démarrage rapide

### 1. Extension Chrome

- Accédez à `chrome://extensions` et activez le mode développeur.
- Cliquez sur "Charger l’extension non empaquetée", puis sélectionnez le dossier `chrome-extension/frontend/`.
- Allez sur une vidéo YouTube, ouvrez l’extension, et obtenez les prédictions de sentiment.

### 2. API Cloud (aucun serveur local nécessaire)

- Endpoint de l’API :
https://adamEl26-Youtube-Comment-analyzer.hf.space/predictbatch
(POST, corps : `{ "comments": ["super vidéo", "mauvaise expérience"] }`)

### 3. Développement local (optionnel)

- Installez les dépendances : `pip install -r requirements.txt`
- Lancez l’API : `uvicorn app:app --reload`
- API disponible sur `http://localhost:8000`

## Organisation du projet

chrome-extension/ # Frontend extension Chrome
models/ # Modèle joblib et vectoriseur
app.py # Backend FastAPI
Dockerfile # Déploiement cloud
requirements.txt # Dépendances Python

## Modèle et performance

- Modèle : TF-IDF + Régression Logistique
- Précision : 86 % (voir rapport)
- L’API traite jusqu’à 100 commentaires en moins de 200 ms

## Auteur

Adam Elmhir (@AdamElmh)

---

**Clonez le projet, installez l’extension et testez-la sur n’importe quelle vidéo YouTube.  
Consultez le rapport technique complet et la démo sur Hugging Face Space pour plus d’infos.**
