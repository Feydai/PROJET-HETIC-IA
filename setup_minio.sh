#!/bin/bash

# Définir les variables
MINIO_ALIAS="myminio"
MINIO_URL="http://localhost:9000"
MINIO_ACCESS_KEY="admin"
MINIO_SECRET_KEY="password"
BUCKET_NAME="documents"
FILE_PATH="data/temp/guide.pdf"

# Configurer l'alias
mc alias set $MINIO_ALIAS $MINIO_URL $MINIO_ACCESS_KEY $MINIO_SECRET_KEY

# Créer le bucket
mc mb $MINIO_ALIAS/$BUCKET_NAME

# Télécharger le fichier PDF
mc cp $FILE_PATH $MINIO_ALIAS/$BUCKET_NAME/
