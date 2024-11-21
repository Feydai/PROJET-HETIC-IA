import os
import PyPDF2
import re
import torch
from minio import Minio
import ollama
import pdfplumber

minio_client = Minio(
    "localhost:9000",
    access_key="admin",
    secret_key="password",
    secure=False
)

VAULT_FILE = "data/vault.txt"
EMBEDDINGS_FILE = "data/vault_embeddings.pt"  # Fichier pour sauvegarder les embeddings
TEMP_DIR = "data/temp/"
os.makedirs(TEMP_DIR, exist_ok=True)  # Crée le répertoire temporaire s'il n'existe pas
BUCKET_NAME = "documents"
OBJECT_NAME = "guide.pdf"  # Remplacez par le nom exact de votre fichier

def load_vault(vault_file):
    if not os.path.exists(vault_file):
        print(f"Le fichier {vault_file} n'existe pas. Assurez-vous qu'il est dans le bon dossier.")
        return []
    with open(vault_file, "r", encoding="utf-8") as f:
        content = [line.strip() for line in f if line.strip()]
    if not content:
        print(f"Le fichier {vault_file} est vide. Ajoutez du contenu pour continuer.")
    return content

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

def generate_embeddings(text_chunks):
    embeddings = []
    for chunk in text_chunks:
        response = ollama.embeddings(model="mxbai-embed-large", prompt=chunk)
        embeddings.append(response["embedding"])
    return torch.tensor(embeddings)

def save_embeddings_to_file(embeddings, file_path):
    torch.save(embeddings, file_path)
    print(f"Embeddings sauvegardés dans {file_path}")

def process_and_save_text(text):
    text = re.sub(r'\s+', ' ', text).strip()  # Normalisation des espaces
    sentences = re.split(r'(?<=[.!?]) +', text)  # Découpage par phrases
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
    return chunks
def process_pdf_from_minio():
    download_path = os.path.join(TEMP_DIR, OBJECT_NAME)

    downloaded_file = download_pdf_from_minio(BUCKET_NAME, OBJECT_NAME, download_path)
    if not downloaded_file:
        print("Impossible de télécharger le fichier PDF.")
        return
    try:
        text = ''
        with pdfplumber.open(downloaded_file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + " "
        chunks = process_and_save_text(text)

        embeddings = generate_embeddings(chunks)
        save_embeddings_to_file(embeddings, EMBEDDINGS_FILE)

        print("Fichier PDF traité et ajouté à vault.txt avec succès.")
    except Exception as e:
        print(f"Erreur lors du traitement du fichier PDF : {e}")

def search_relevant_context(question):
    if not os.path.exists(EMBEDDINGS_FILE):
        print(f"Le fichier {EMBEDDINGS_FILE} est introuvable. Traitez un fichier PDF d'abord.")
        return

    vault_content = load_vault(VAULT_FILE)
    if not vault_content:
        print("Le vault est vide. Ajoutez du contenu pour continuer.")
        return

    embeddings = torch.load(EMBEDDINGS_FILE, weights_only=True)
    input_embedding = torch.tensor(ollama.embeddings(model="mxbai-embed-large", prompt=question)["embedding"]).unsqueeze(0)
    similarities = torch.cosine_similarity(input_embedding, embeddings)
    top_indices = torch.topk(similarities, k=min(3, len(similarities))).indices.tolist()

    print("\nContexte pertinent :")
    for idx in top_indices:
        print(f"- {vault_content[idx]}")
