import boto3

MINIO_ENDPOINT = "http://minio:9000"
MINIO_ACCESS_KEY = "minioadmin"
MINIO_SECRET_KEY = "minioadmin123"

s3_client = boto3.client(
    "s3",
    endpoint_url=MINIO_ENDPOINT,
    aws_access_key_id=MINIO_ACCESS_KEY,
    aws_secret_access_key=MINIO_SECRET_KEY
)

print("Liste des buckets disponibles :")
buckets = s3_client.list_buckets()
for bucket in buckets.get("Buckets", []):
    print(f"- {bucket['Name']}")

bucket_name = "minio-test-bucket"
try:
    s3_client.create_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' créé avec succès.")
except s3_client.exceptions.BucketAlreadyExists:
    print(f"Le bucket '{bucket_name}' existe déjà.")

file_name = "example.txt"
with open(file_name, "w") as f:
    f.write("Ceci est un fichier de test pour MinIO connecté à S3.")

s3_client.upload_file(file_name, bucket_name, file_name)
print(f"Fichier '{file_name}' téléchargé dans le bucket '{bucket_name}'.")

print(f"Contenu du bucket '{bucket_name}' :")
objects = s3_client.list_objects_v2(Bucket=bucket_name)
for obj in objects.get("Contents", []):
    print(f"- {obj['Key']}")
