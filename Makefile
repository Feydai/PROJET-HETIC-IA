SHELL := /bin/bash

COMPOSE_FILE=docker-compose.yml
REQUIREMENTS_FILE=requirements.txt

.PHONY: build up down logs stop py py-activate run

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

# Exécuter une commande dans l'environnement virtuel
run:
	@if [ ! -d .venv ]; then \
		echo "Création de l'environnement virtuel..."; \
		python3 -m venv .venv || { echo "Erreur lors de la création de l'environnement virtuel."; exit 1; }; \
	fi; \
	echo "Activation de l'environnement virtuel..."; \
	. .venv/bin/activate && \
	echo "Mise à jour de pip..."; \
	pip install --upgrade pip || { echo "Erreur lors de la mise à jour de pip."; exit 1; }; \
	if [ -f $(REQUIREMENTS_FILE) ]; then \
		echo "Installation des dépendances..."; \
		pip install -r $(REQUIREMENTS_FILE) || { echo "Erreur lors de l'installation des dépendances."; exit 1; }; \
	fi; \
	echo "Exécution du script..."; \
	python app/main.py || { echo "Erreur lors de l'exécution du script."; exit 1; };