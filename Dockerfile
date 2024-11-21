FROM python:3.9-slim

WORKDIR /app

RUN python3 -m venv /app/env

RUN /app/env/bin/pip install --upgrade pip

COPY . .

ENV PATH="/app/env/bin:$PATH"

CMD ["/bin/bash"]
