# Chatbot RAG avec Streamlit et Google Cloud Storage

Un chatbot interactif utilisant la technique **RAG (Retrieval-Augmented Generation)** pour fournir des réponses précises à partir de documents PDF stockés dans Google Cloud Storage. Ce projet compare les performances **avec** et **sans RAG**.

---

## Fonctionnalités

- **Récupération des documents** : Téléchargement et traitement des fichiers PDF depuis Google Cloud Storage.
- **RAG** : Construction d'un index pour enrichir les réponses du chatbot avec des informations spécifiques.
- **Comparaison** : Réponses générées **avec RAG** vs **sans RAG**.
- **Température ajustable** : Contrôler la créativité des réponses en ajustant la température du modèle.

---

## Technologies utilisées

- **Langages et outils** :
  - Python (3.9+)
  - [Streamlit](https://streamlit.io/) pour l'interface utilisateur.
  - [Google Cloud Storage](https://cloud.google.com/storage) pour stocker les documents.
  - [LangChain](https://www.langchain.com/) pour le pipeline RAG.
  - [OpenAI API](https://platform.openai.com/) pour les modèles LLM.

- **Bibliothèques Python** :
  - `streamlit`
  - `langchain`
  - `openai`
  - `google-cloud-storage`
  - `PyPDF2`
  - `tiktoken`
  - `python-dotenv`

---

## Prérequis

1. **Google Cloud** :
   - Créez un bucket Google Cloud Storage.
   - Configurez un compte de service avec le rôle `Storage Object Viewer`.
   - Téléchargez le fichier `service_account.json` et configurez l'accès.

2. **Clé API OpenAI** :
   - Générez une clé API sur [OpenAI API Keys](https://platform.openai.com/account/api-keys).
   - Ajoutez-la dans le fichier `.env`.

---

## Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/siraKLG/chatbot-rag.git
   cd chatbot-rag
