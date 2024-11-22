from google.cloud import storage
import os
from PyPDF2 import PdfReader
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

def download_pdf_from_gcs(bucket_name, file_name, destination_folder="./tmp"):
    """Télécharge un fichier PDF depuis un bucket Google Cloud Storage."""
    os.makedirs(destination_folder, exist_ok=True)  # Crée un dossier temporaire si nécessaire
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    local_path = os.path.join(destination_folder, os.path.basename(file_name))
    blob.download_to_filename(local_path)
    return local_path

def extract_text_from_pdf(pdf_path):
    """Extrait le texte d'un fichier PDF."""
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def fetch_pdfs_from_gcs(bucket_name, prefix, destination_folder="./tmp"):
    """Télécharge tous les fichiers PDF depuis un bucket avec un préfixe."""
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=prefix)

    docs = []
    for blob in blobs:
        if blob.name.endswith(".pdf"):
            local_path = download_pdf_from_gcs(bucket_name, blob.name, destination_folder)
            docs.append(extract_text_from_pdf(local_path))
    return docs

def build_index(docs):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(docs, embeddings)
    return vectorstore

def generate_response(query, index, temperature=0.7):
    if not hasattr(index, "as_retriever"):
        raise ValueError("L'objet index fourni n'est pas valide. Assurez-vous qu'il a été créé correctement.")
    
    retriever = index.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(
        llm=OpenAI(model_name="text-davinci-003", temperature=temperature),
        retriever=retriever
    )
    return qa_chain.run(query)