import ollama
from ollama import Message

def ollama_chat_without_rag(user_input, model="llama3.2"):
    """
    Interacts directly with the Ollama model without contextual search.

    Args:
        user_input (str): The user's question or prompt.
        model (str): The Ollama model to use (default: llama3.2).

    Returns:
        str: The response from the Ollama model.
    """
    try:
        messages = [Message(role="user", content=user_input)]
        response = ollama.chat(model=model, messages=messages)
        return response['message']['content']
    except Exception as e:
        print(f"Error interacting with Ollama: {e}")
        return "Error generating the response."
