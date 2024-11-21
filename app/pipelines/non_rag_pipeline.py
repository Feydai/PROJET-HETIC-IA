from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import Ollama
from langchain.chains import RetrievalQA

def rag_pipeline(chunks, question, model="llama2", temperature=0.7):
    """Pipeline RAG utilisant Ollama."""
    # Indexer les documents avec FAISS
    embeddings = HuggingFaceEmbeddings()
    vector_store = FAISS.from_texts(chunks, embeddings)

    # Configurer Ollama
    llm = Ollama(model=model, temperature=temperature)

    # Configurer RetrievalQA
    retriever = vector_store.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=True
    )

    # Poser la question
    response = qa_chain.run(question)
    return response
