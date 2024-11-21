FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y python3-venv && apt-get clean

RUN python3 -m venv /app/env

RUN /app/env/bin/pip install --upgrade pip

COPY . .

ENV PATH="/app/env/bin:$PATH"

RUN pip install --no-cache-dir -r requirements.txt

CMD ["/bin/bash"]

