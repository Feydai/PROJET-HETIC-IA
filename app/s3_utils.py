import boto3

MINIO_ENDPOINT = "http://127.0.0.1:9000"
ACCESS_KEY = "minioadmin"
SECRET_KEY = "minioadmin"

s3_client = boto3.client(
    "s3",
    endpoint_url=MINIO_ENDPOINT,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)

def list_files_s3(bucket_name):
    """Lister les fichiers dans un bucket S3."""
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        return [obj['Key'] for obj in response.get('Contents', [])]
    except Exception as e:
        print(f"Erreur lors de la récupération des fichiers dans S3 : {e}")
        return []

def download_file_s3(bucket_name, object_name, destination):
    """Télécharger un fichier depuis S3."""
    try:
        s3_client.download_file(bucket_name, object_name, destination)
        print(f"Fichier '{object_name}' téléchargé dans '{destination}'.")
    except Exception as e:
        print(f"Erreur lors du téléchargement depuis S3 : {e}")

def upload_file_s3(bucket_name, object_name, file_path):
    """Uploader un fichier vers S3."""
    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"Fichier '{file_path}' uploadé avec succès dans S3 (bucket: {bucket_name}).")
    except Exception as e:
        print(f"Erreur lors de l'upload vers S3 : {e}")
