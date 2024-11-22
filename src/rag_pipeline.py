from google.cloud import storage
import PyPDF2

def fetch_documents(bucket_name, prefix):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=prefix)

    docs = []
    for blob in blobs:
        if blob.name.endswith('.pdf'):
            content = blob.download_as_bytes()
            docs.append(parse_pdf(content))
    return docs

def parse_pdf(content):
    pdf_reader = PyPDF2.PdfReader(content)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text
