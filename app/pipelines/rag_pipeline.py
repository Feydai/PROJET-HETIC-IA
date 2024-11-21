from langchain.llms import Ollama

def no_rag_pipeline(question, model="llama2", temperature=0.7):
    """Pipeline sans contexte, question posée directement à Ollama."""
    llm = Ollama(model=model, temperature=temperature)

    response = llm(question)
    return response
