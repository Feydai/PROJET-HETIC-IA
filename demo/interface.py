import streamlit as st
from app.pipelines.non_rag_pipeline import non_rag_pipeline
from app.pipelines.rag_pipeline import rag_pipeline

st.title("Chatbot avec et sans RAG")

question = st.text_input("Posez une question :")
temperature = st.slider("Réglez la température :", 0.0, 1.0, 0.7)

if st.button("Réponse sans RAG"):
    response = non_rag_pipeline(question, temperature=temperature)
    st.write("Réponse :", response)

if st.button("Réponse avec RAG"):
    response = rag_pipeline("documents", question, temperature=temperature)
    st.write("Réponse :", response)
