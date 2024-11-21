COMPOSE_FILE=docker-compose.yml
REQUIREMENTS_FILE=requirements.txt

.PHONY: build up down logs install

build:
	docker compose -f $(COMPOSE_FILE) up --build

up:
	docker compose -f $(COMPOSE_FILE) up -d

down:
	docker compose -f $(COMPOSE_FILE) down

logs:
	docker compose -f $(COMPOSE_FILE) logs -f

stop:
	docker system prune -a --volumes -f
