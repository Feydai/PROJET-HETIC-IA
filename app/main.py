import os
from ..minio_utils import download_pdf_from_minio
from ..pdf_to_text import convert_pdf_to_chunks
from ..pipelines.rag_pipeline import rag_pipeline
from ..pipelines.no_rag_pipeline import no_rag_pipeline

def main():
    print("=== Pipeline IA : Mode RAG ou No RAG ===\n")

    mode = input("Choisissez le mode ('rag' ou 'no-rag') [par défaut : rag] : ").strip().lower()
    if mode not in ["rag", "no-rag", ""]:
        print("Mode invalide. Veuillez choisir 'rag' ou 'no-rag'.")
        return
    mode = mode or "rag"

    model = "llama2"
    temperature = float(input("Réglez la température (0.0 à 1.0) [par défaut : 0.7] : ") or 0.7)

    # Poser la question
    question = input("Posez votre question : ")
    
    if mode == "rag":
        bucket_name = "documents"
        object_name = "example.pdf"
        pdf_path = "/tmp/example.pdf"

        download_pdf_from_minio(bucket_name, object_name, pdf_path)

        chunks = convert_pdf_to_chunks(pdf_path)
        print(f"PDF converti en {len(chunks)} chunks.")

        response = rag_pipeline(chunks, question, model=model, temperature=temperature)
    else:
        response = no_rag_pipeline(question, model=model, temperature=temperature)

    print("\nRéponse :")
    print(response)

if __name__ == "__main__":
    main()
