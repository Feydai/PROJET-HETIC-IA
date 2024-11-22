FROM debian:bullseye-slim

RUN apt-get update && apt-get install -y curl wget bash && rm -rf /var/lib/apt/lists/*

RUN wget https://dl.min.io/client/mc/release/linux-amd64/mc -O /usr/bin/mc && \
    chmod +x /usr/bin/mc

COPY setup-minio.sh /usr/local/bin/setup-minio.sh

RUN chmod +x /usr/local/bin/setup-minio.sh

ENTRYPOINT ["/usr/local/bin/setup-minio.sh"]
