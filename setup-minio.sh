#!/bin/bash

# Définir les variables
MINIO_ALIAS="myminio"
MINIO_URL=${MINIO_URL:-"http://minio:9000"}
MINIO_ACCESS_KEY=${MINIO_ROOT_USER:-"admin"}
MINIO_SECRET_KEY=${MINIO_ROOT_PASSWORD:-"password"}
BUCKET_NAME=${BUCKET_NAME:-"documents"}
FILE_PATH=${FILE_PATH:-"/data/temp/guide.pdf"}

# Attendre que le service MinIO soit prêt
echo "En attente de la disponibilité de MinIO..."
until curl -s $MINIO_URL/minio/health/ready > /dev/null; do
  echo "MinIO n'est pas encore prêt. Réessai dans 5 secondes..."
  sleep 5
done

# Configurer l'alias
mc alias set $MINIO_ALIAS $MINIO_URL $MINIO_ACCESS_KEY $MINIO_SECRET_KEY

# Créer le bucket
mc mb $MINIO_ALIAS/$BUCKET_NAME

# Télécharger le fichier PDF
mc cp $FILE_PATH $MINIO_ALIAS/$BUCKET_NAME

echo "Configuration terminée avec succès."
