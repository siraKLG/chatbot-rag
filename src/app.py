import streamlit as st
from rag_pipeline import generate_response_with_rag
from no_rag_pipeline import generate_response_without_rag

# Titre de l'application
st.title("Comparaison Chatbot : Avec RAG vs Sans RAG")

# Entrée utilisateur
query = st.text_input("Posez votre question :")
temperature = st.slider("Température LLM", min_value=0.0, max_value=1.0, value=0.7)

# Bouton pour lancer la comparaison
if st.button("Comparer les résultats"):
    with st.spinner("Génération de réponses..."):
        rag_response = generate_response_with_rag(query, temperature)
        no_rag_response = generate_response_without_rag(query, temperature)
    
    # Affichage des résultats
    st.subheader("Réponse Sans RAG")
    st.write(no_rag_response)
    
    st.subheader("Réponse Avec RAG")
    st.write(rag_response)
