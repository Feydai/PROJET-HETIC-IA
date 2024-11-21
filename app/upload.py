import os
import PyPDF2
import re
from minio import Minio

# Configuration MinIO
minio_client = Minio(
    "localhost:9000",
    access_key="admin",
    secret_key="password",
    secure=False
)

VAULT_FILE = "data/vault.txt"
TEMP_DIR = "data/temp/"
os.makedirs(TEMP_DIR, exist_ok=True)

BUCKET_NAME = "documents"
OBJECT_NAME = "guide.pdf"

def download_pdf_from_minio(bucket_name, object_name, download_path):
    try:
        minio_client.fget_object(bucket_name, object_name, download_path)
        print(f"Fichier {object_name} téléchargé depuis le bucket {bucket_name} à {download_path}.")
        return download_path
    except Exception as e:
        print(f"Erreur lors du téléchargement depuis MinIO : {e}")
        return None

def save_to_vault(text):
    with open(VAULT_FILE, "a", encoding="utf-8") as vault_file:
        vault_file.write(text.strip() + "\n")
    print(f"Contenu ajouté à {VAULT_FILE}.")

def process_and_save_text(text):
    text = re.sub(r'\s+', ' ', text).strip()
    sentences = re.split(r'(?<=[.!?]) +', text)
    chunks = []
    current_chunk = ""
    for sentence in sentences:
        if len(current_chunk) + len(sentence) + 1 < 1000:
            current_chunk += (sentence + " ").strip()
        else:
            chunks.append(current_chunk)
            current_chunk = sentence + " "
    if current_chunk:
        chunks.append(current_chunk)
    for chunk in chunks:
        save_to_vault(chunk.strip())

def process_pdf_from_minio():
    download_path = os.path.join(TEMP_DIR, OBJECT_NAME)

    downloaded_file = download_pdf_from_minio(BUCKET_NAME, OBJECT_NAME, download_path)
    if not downloaded_file:
        print("Impossible de télécharger le fichier PDF.")
        return

    try:
        with open(downloaded_file, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ''
            for page in pdf_reader.pages:
                if page.extract_text():
                    text += page.extract_text() + " "
        process_and_save_text(text)
        print("Fichier PDF traité et ajouté à vault.txt avec succès.")
    except Exception as e:
        print(f"Erreur lors du traitement du fichier PDF : {e}")

# Exécuter le traitement
if __name__ == "__main__":
    process_pdf_from_minio()
