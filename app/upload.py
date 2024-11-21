import os
import PyPDF2
import re
from minio import Minio

# Configuration MinIO
minio_client = Minio(
    "localhost:9000",  # MinIO URL
    access_key="admin",  # Remplacez par votre username
    secret_key="password",  # Remplacez par votre password
    secure=False  # True si SSL est activé
)

# Chemins pour le traitement
VAULT_FILE = "data/vault.txt"
TEMP_DIR = "data/temp/"
os.makedirs(TEMP_DIR, exist_ok=True)  # Crée le répertoire temporaire s'il n'existe pas

# Nom du fichier PDF dans le bucket MinIO
BUCKET_NAME = "documents"
OBJECT_NAME = "guide.pdf"  # Remplacez par le nom exact de votre fichier

# Fonction pour télécharger un fichier depuis MinIO
def download_pdf_from_minio(bucket_name, object_name, download_path):
    try:
        minio_client.fget_object(bucket_name, object_name, download_path)
        print(f"Fichier {object_name} téléchargé depuis le bucket {bucket_name} à {download_path}.")
        return download_path
    except Exception as e:
        print(f"Erreur lors du téléchargement depuis MinIO : {e}")
        return None

# Fonction pour sauvegarder le texte dans vault.txt
def save_to_vault(text):
    with open(VAULT_FILE, "a", encoding="utf-8") as vault_file:
        vault_file.write(text.strip() + "\n")
    print(f"Contenu ajouté à {VAULT_FILE}.")

# Fonction pour traiter le texte en chunks de 1000 caractères
def process_and_save_text(text):
    text = re.sub(r'\s+', ' ', text).strip()  # Normalisation des espaces
    sentences = re.split(r'(?<=[.!?]) +', text)  # Découpage par phrases
    chunks = []
    current_chunk = ""
    for sentence in sentences:
        if len(current_chunk) + len(sentence) + 1 < 1000:  # +1 pour l'espace
            current_chunk += (sentence + " ").strip()
        else:
            chunks.append(current_chunk)
            current_chunk = sentence + " "
    if current_chunk:
        chunks.append(current_chunk)
    for chunk in chunks:
        save_to_vault(chunk.strip())

# Fonction principale pour télécharger, convertir et sauvegarder le PDF
def process_pdf_from_minio():
    download_path = os.path.join(TEMP_DIR, OBJECT_NAME)

    # Télécharger le fichier depuis MinIO
    downloaded_file = download_pdf_from_minio(BUCKET_NAME, OBJECT_NAME, download_path)
    if not downloaded_file:
        print("Impossible de télécharger le fichier PDF.")
        return

    # Extraire le texte du PDF
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
