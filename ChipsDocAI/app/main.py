# app/main.py
import streamlit as st
from backend.pdf_processor import extract_text_chunks
from backend.embedder import embed_chunks
from backend.vector_store import get_similar_chunks
from backend.query_engine import answer_question

st.set_page_config(page_title="ChipDocs AI")
st.title("📘 ChipDocs AI")

uploaded_file = st.file_uploader("Upload a chip datasheet PDF")
question = st.text_input("Ask a question about this document")

if uploaded_file and question:
    with st.spinner("Processing PDF..."):
        chunks = extract_text_chunks(uploaded_file)
        embed_chunks(chunks)
    with st.spinner("Thinking..."):
        results = get_similar_chunks(question)
        response = answer_question(question, results)
        st.markdown("### 📎 Answer")
        st.write(response)
        st.markdown("### 📄 Sources")
        for i, r in enumerate(results):
            st.write(f"{i+1}. {r}")

# backend/pdf_processor.py
import fitz

def extract_text_chunks(pdf_file, chunk_size=500):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    full_text = "\n".join([page.get_text() for page in doc])
    return [full_text[i:i+chunk_size] for i in range(0, len(full_text), chunk_size)]

# backend/embedder.py
import openai
import os
from dotenv import load_dotenv
load_dotenv()

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")
VECTOR_DB = []

def embed_chunks(chunks):
    global VECTOR_DB
    VECTOR_DB = [
        {
            "text": chunk,
            "embedding": openai.Embedding.create(
                input=chunk,
                model=EMBEDDING_MODEL
            )["data"][0]["embedding"]
        }
        for chunk in chunks
    ]

# backend/vector_store.py
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from backend.embedder import VECTOR_DB, embed_chunks
import openai
import os

def get_similar_chunks(query, top_k=5):
    query_embedding = openai.Embedding.create(
        input=query,
        model=os.getenv("EMBEDDING_MODEL")
    )["data"][0]["embedding"]
    similarities = [
        (chunk["text"], cosine_similarity([query_embedding], [chunk["embedding"]])[0][0])
        for chunk in VECTOR_DB
    ]
    sorted_chunks = sorted(similarities, key=lambda x: x[1], reverse=True)
    return [text for text, _ in sorted_chunks[:top_k]]

# backend/query_engine.py
import openai
import os
from dotenv import load_dotenv
load_dotenv()

GPT_MODEL = os.getenv("GPT_MODEL")

def answer_question(question, context_chunks):
    context = "\n".join(context_chunks)
    prompt = f"""
You are an expert chip documentation assistant.
Given the following context, answer the user's question clearly, citing source text when needed.

Context:
{context}

Question: {question}
"""
    response = openai.ChatCompletion.create(
        model=GPT_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return response.choices[0].message.content
