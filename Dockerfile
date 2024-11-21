FROM python:3.9-slim

WORKDIR /app

RUN python3 -m venv /app/env

COPY . .

CMD ["/bin/bash", "-c", "source /app/env/bin/activate && exec /bin/bash"]