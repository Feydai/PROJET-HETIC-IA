from rag import process_pdf_from_minio, search_relevant_context
from no_rag import ollama_chat_without_rag

def main():
    print("\nBienvenue dans l'application de recherche contextuelle avec Ollama !")
    print("Choisissez une option :")
    print("1. Traiter un fichier PDF depuis MinIO (Préparer le Vault)")
    print("2. Rechercher un contexte pertinent avec RAG")
    print("3. Chat sans RAG (Interaction directe)")
    print("Tapez 'quit' pour quitter.")

    while True:
        # Afficher le menu principal
        choice = input("\nVotre choix (1, 2 ou 3) : ").strip()
        if choice.lower() == "quit":
            print("Merci d'avoir utilisé cette application. À bientôt !")
            break

        try:
            if choice == "1":
                # Traiter un fichier PDF depuis MinIO
                print("\nTraitement du fichier PDF depuis MinIO...")
                process_pdf_from_minio()
            elif choice == "2":
                # Recherche contextuelle avec RAG
                question = input("\nEntrez votre question : ")
                print("\nRecherche de contexte pertinent avec RAG...")
                search_relevant_context(question)
            elif choice == "3":
                # Interaction directe avec Ollama (No RAG)
                question = input("\nEntrez votre question pour No RAG : ")
                print("\nInteraction directe avec Ollama...")
                response = ollama_chat_without_rag(question)
                print(f"\nRéponse : {response}")
            else:
                # Gestion des choix invalides
                print("Choix invalide. Veuillez entrer '1', '2' ou '3'.")
        except Exception as e:
            # Gestion des erreurs
            print(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    main()
