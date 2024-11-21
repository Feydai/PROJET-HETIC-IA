from minio import Minio

client = Minio(
    "localhost:9000",
    access_key="admin",
    secret_key="password",
    secure=False
)

def list_files_minio(bucket_name):
    """Lister les fichiers disponibles dans un bucket MinIO."""
    try:
        return [obj.object_name for obj in client.list_objects(bucket_name)]
    except Exception as e:
        print(f"Erreur lors de la récupération des fichiers dans MinIO : {e}")
        return []

def download_file_minio(bucket_name, object_name, destination):
    """Télécharger un fichier depuis MinIO."""
    try:
        client.fget_object(bucket_name, object_name, destination)
        print(f"Fichier '{object_name}' téléchargé dans '{destination}'.")
    except Exception as e:
        print(f"Erreur lors du téléchargement depuis MinIO : {e}")

def upload_file_minio(bucket_name, object_name, file_path):
    """Uploader un fichier vers MinIO."""
    try:
        client.fput_object(bucket_name, object_name, file_path)
        print(f"Fichier '{file_path}' uploadé avec succès dans MinIO (bucket: {bucket_name}).")
    except Exception as e:
        print(f"Erreur lors de l'upload vers MinIO : {e}")
