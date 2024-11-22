# **PROJET-HETIC-IA**

Bienvenue dans le **PROJET-HETIC-IA** !

## **Fonctionnalités principales**

1. **Recherche contextuelle avec RAG**
   - Utilise **MinIO** pour stocker des fichiers PDF.
   - Recherche et analyse des fichiers pour des réponses pertinentes.

2. **Chat sans RAG**
   - Interaction directe avec **Ollama**, un modèle d'intelligence artificielle.

3. **Gestion d'environnements virtuels Python**
   - Crée et configure un environnement Python dédié pour le projet.

4. **Téléchargement de modèles avec Ollama**
   - Télécharge et configure le modèle **xbaim** pour les tâches de génération.

5. **Gestion des services avec Docker Compose**
   - Configure et exécute des services nécessaires au projet.

---

## **Prérequis**

Avant de commencer, assurez-vous d’avoir installé les outils suivants :

- **Python** (>= 3.8)
- **Docker** et **Docker Compose**
- **Make** (outil de gestion de tâches)
- **Ollama** ([Téléchargez ici](https://ollama.com))
- **Git**

---

## **Installation et Utilisation**

   **Cloner le projet** :

   ```bash
   git clone https://github.com/Feydai/PROJET-HETIC-IA.git
   cd PROJET-HETIC-I
   ```

   **Démarrer les services Docker**

   Étape 1 : Démarrer les services Docker
   Exécutez la commande suivante pour lancer les services nécessaires :

   ```bash
   make up
   ```

   **Installer les dépendances**

   Étape 2 : Exécuter l'application
   Une fois les services en cours d’exécution, lancez l’application principale :

   ```bash
   make run
   ```

   **Arreter les services Docker**

   Étape 3 : Arrêter les services Docker
   Lorsque vous avez terminé, arrêtez les services Docker avec :

   ```bash
   make down
   ```
   ### **Commandes disponibles**
   
   | Commande | Description |
   | --- | --- |
   | `make up` | Démarre les services Docker (MinIO, etc.). |
   | `make down` | Arrête et supprime les services Docker en cours d’exécution. |
   | `make logs` | Affiche les logs des services Docker. |
   | `make run` | Exécute tout le projet (environnement, dépendances, script principal). |

   ### **À propos des fichiers**

   - **app/main.py** : Point d’entrée principal de l’application..
   - **app/rag.py** : Contient les fonctions liées à la recherche contextuelle avec RAG..
   - **docker-compose.yml** : Fichier de configuration Docker Compose..
   - **requirements.txt** : Liste des dépendances Python nécessaires..
   - **Makefile** : Automatisation des tâches courantes..

   ### **Contributeurs**
   
   **SUN Léo**

