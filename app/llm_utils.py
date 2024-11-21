from langchain.llms import Ollama

llm = Ollama(
    model="llama2",
    temperature=0.7
)
