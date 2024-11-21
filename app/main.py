from rag import process_pdf_from_minio, search_relevant_context
from no_rag import ollama_chat_without_rag
from llm_config import llm_config
import traceback
from colorama import Fore, Style, init

# Initialisation de colorama pour Windows (inutile sur Linux/Mac, mais sans danger)
init(autoreset=True)

def main():
    """
    Interface principale de l'application.
    """
    while True:
        print(f"\n{Fore.CYAN}Bienvenue dans l'application de recherche contextuelle avec Ollama !")
        print(f"{Fore.YELLOW}Choisissez une option :")
        print(f"{Fore.GREEN}1. {Fore.RESET}Traiter un fichier PDF depuis MinIO (Préparer le Vault)")
        print(f"{Fore.GREEN}2. {Fore.RESET}Rechercher un contexte pertinent avec RAG")
        print(f"{Fore.GREEN}3. {Fore.RESET}Chat sans RAG (Interaction directe)")
        print(f"{Fore.GREEN}4. {Fore.RESET}Changer la température du LLM ({Fore.CYAN}Température actuelle : {llm_config.get_temperature():.1f}{Fore.RESET})")
        print(f"{Fore.RED}Tapez 'quit' pour quitter.")

        choice = input(f"\n{Fore.BLUE}Votre choix (1, 2, 3 ou 4) : {Fore.RESET}").strip()

        if choice.lower() == "quit":
            confirm = input(f"{Fore.RED}Êtes-vous sûr de vouloir quitter ? (oui/non) : {Fore.RESET}").strip().lower()
            if confirm == "oui":
                print(f"{Fore.MAGENTA}Merci d'avoir utilisé cette application. À bientôt !")
                break
            else:
                print(f"{Fore.CYAN}Retour au menu principal.")
                continue

        try:
            if choice == "1":
                print(f"\n{Fore.GREEN}Traitement du fichier PDF depuis MinIO...{Fore.RESET}")
                process_pdf_from_minio()
                print(f"{Fore.CYAN}Traitement terminé avec succès !{Fore.RESET}")
            elif choice == "2":
                question = input(f"\n{Fore.BLUE}Entrez votre question : {Fore.RESET}").strip()
                if not question:
                    print(f"{Fore.RED}La question ne peut pas être vide. Veuillez réessayer.{Fore.RESET}")
                    continue
                print(f"\n{Fore.GREEN}Recherche de contexte pertinent avec RAG...{Fore.RESET}")
                search_relevant_context(question)
            elif choice == "3":
                question = input(f"\n{Fore.BLUE}Entrez votre question pour No RAG : {Fore.RESET}").strip()
                if not question:
                    print(f"{Fore.RED}La question ne peut pas être vide. Veuillez réessayer.{Fore.RESET}")
                    continue
                print(f"\n{Fore.GREEN}Interaction directe avec Ollama...{Fore.RESET}")
                try:
                    response = ollama_chat_without_rag(
                        user_input=question,
                        model="llama3.2",
                        temperature=llm_config.get_temperature()
                    )
                    print(f"\n{Fore.YELLOW}Réponse : {Fore.RESET}{response}")
                except Exception as e:
                    print(f"{Fore.RED}Erreur lors de l'interaction avec Ollama : {e}{Fore.RESET}")
            elif choice == "4":
                new_temp = input(f"\n{Fore.BLUE}Entrez une nouvelle température (entre 0.0 et 1.5) : {Fore.RESET}").strip()
                try:
                    new_temp = float(new_temp)
                    if 0.0 <= new_temp <= 1.5:
                        llm_config.set_temperature(new_temp)
                        print(f"{Fore.CYAN}Température mise à jour à {new_temp:.1f}.{Fore.RESET}")
                    else:
                        print(f"{Fore.RED}La température doit être entre 0.0 et 1.5. Veuillez réessayer.{Fore.RESET}")
                except ValueError:
                    print(f"{Fore.RED}Entrée invalide. Veuillez entrer un nombre entre 0.0 et 1.5.{Fore.RESET}")
            else:
                print(f"{Fore.RED}Choix invalide. Veuillez entrer '1', '2', '3' ou '4'.{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}Une erreur s'est produite : {e}{Fore.RESET}")
            print(f"{Fore.YELLOW}Détails de l'erreur :{Fore.RESET}")
            traceback.print_exc()

if __name__ == "__main__":
    main()
