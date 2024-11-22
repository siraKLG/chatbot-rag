from dotenv import load_dotenv
import os
load_dotenv()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
import streamlit as st
from rag_pipeline import build_index, generate_response, fetch_pdfs_from_gcs
from no_rag_pipeline import generate_response_without_rag

openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("La clé API OpenAI n'est pas configurée.")

BUCKET_NAME = "rag-project221"
PREFIX = "pdfs/"

docs = fetch_pdfs_from_gcs(BUCKET_NAME, PREFIX)

index = build_index(docs)

# Titre de l'application
st.title("Comparaison Chatbot : Avec RAG vs Sans RAG")

# Entrée utilisateur
query = st.text_input("Posez votre question :")
temperature = st.slider("Température LLM", 0.0, 1.0, 0.7)


# Bouton pour lancer la comparaison
if st.button("Comparer les résultats"):
    with st.spinner("Génération de réponses..."):
        rag_response = generate_response(query, index, temperature)
        print("Réponse avec RAG :", rag_response)
        no_rag_response = generate_response_without_rag(query, temperature)

    
    # Affichage des résultats
    st.subheader("Réponse Sans RAG")
    st.write(no_rag_response)
    
    st.subheader("Réponse Avec RAG")
    st.write(rag_response)
