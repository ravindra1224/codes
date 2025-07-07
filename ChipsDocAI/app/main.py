import streamlit as st
from backend.pdf_processor import extract_text_chunks
from backend.embedder import embed_chunks
from backend.vector_store import get_similar_chunks
from backend.query_engine import answer_question

st.set_page_config(page_title="ChipDocs AI")
st.title("📘 ChipDocs AI")

uploaded_file = st.file_uploader("Upload a chip datasheet PDF")
question = st.text_input("Ask a question about this document")
