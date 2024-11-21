import ollama
from ollama import Message
import traceback

def ollama_chat_without_rag(user_input: str, model: str = "llama3.2", temperature: float = 0.7):
    """
    Fonction pour interagir directement avec Ollama sans utiliser RAG.
    """
    try:
        # Validation des types
        if not isinstance(user_input, str) or not user_input.strip():
            raise ValueError(f"L'entrée utilisateur doit être une chaîne non vide. Valeur reçue : {user_input}")
        if not isinstance(model, str):
            raise ValueError(f"Le modèle doit être une chaîne (string). Valeur reçue : {model}")
        if not isinstance(temperature, (float, int)) or not (0.0 <= temperature <= 1.5):
            raise ValueError(f"La température doit être un nombre entre 0.0 et 1.5. Valeur reçue : {temperature}")

        # Log de débogage
        print(f"Modèle reçu : {model}, Type : {type(model)}")
        print(f"Température reçue : {temperature}, Type : {type(temperature)}")
        print(f"Prompt utilisateur : {repr(user_input)}")

        # Construire le message pour le modèle
        instruction = f"Réponds avec une créativité adaptée à une température de {temperature:.1f}."
        messages = [
            Message(role="system", content=instruction),
            Message(role="user", content=user_input)
        ]

        # Appeler Ollama
        response = ollama.chat(
            model=model,
            messages=messages
        )

        # Vérification de la réponse
        if not response or 'message' not in response or 'content' not in response['message']:
            raise ValueError(f"Réponse inattendue d'Ollama : {response}")

        # Retourner la réponse générée
        return response['message']['content']

    except ValueError as ve:
        print(f"Erreur de validation : {ve}")
        return str(ve)
    except Exception as e:
        print(f"Erreur lors de l'interaction avec Ollama : {e}")
        traceback.print_exc()
        return f"Erreur lors de la génération de la réponse : {str(e)}"