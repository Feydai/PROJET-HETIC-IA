# Utiliser une image Debian comme base
FROM debian:bullseye-slim

# Installer curl, mc et autres dépendances
RUN apt-get update && apt-get install -y curl wget bash && rm -rf /var/lib/apt/lists/*

# Télécharger le client MinIO (mc)
RUN wget https://dl.min.io/client/mc/release/linux-amd64/mc -O /usr/bin/mc && \
    chmod +x /usr/bin/mc

# Copier le script dans le conteneur
COPY setup-minio.sh /usr/local/bin/setup-minio.sh

# Rendre le script exécutable
RUN chmod +x /usr/local/bin/setup-minio.sh

# Définir le point d'entrée
ENTRYPOINT ["/usr/local/bin/setup-minio.sh"]
