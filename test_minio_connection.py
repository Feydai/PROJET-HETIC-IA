from minio import Minio

def test_minio_connection():
    client = Minio(
        "minio:9000",
        access_key="admin",
        secret_key="password",
        secure=False
    )

    try:
        buckets = client.list_buckets()
        print("Connexion réussie. Voici les buckets disponibles :")
        for bucket in buckets:
            print(f"- {bucket.name}")
        return True
    except Exception as e:
        print("Erreur lors de la connexion à MinIO :", e)
        return False

if __name__ == "__main__":
    if test_minio_connection():
        print("Test réussi : Connexion à MinIO opérationnelle.")
    else:
        print("Test échoué : Impossible de se connecter à MinIO.")
