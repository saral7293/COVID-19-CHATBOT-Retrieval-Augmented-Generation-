import streamlit as st
import os
import io
import argparse
from dataclasses import dataclass
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain.vectorstores.chroma import Chroma
import shutil
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

logging.getLogger('streamlit').setLevel(logging.ERROR)
CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

st.title("Covid-19 Chatbot")

# Function to query response and handle user interaction
def query_res(query_text, db, current_position):
    # Search the DB.
    results = db.similarity_search_with_relevance_scores(query_text, k=3)

    # If no relevant results found, directly respond with "I don't have enough information"
    if len(results) == 0:
        st.write("I don't have enough information about this. The context of this information is outside of the uploaded PDF.")
        return

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    model = ChatOpenAI()
    response_ai = model.invoke(prompt)

    # Convert AIMessage object to string
    response_text = str(response_ai)

    sources = [doc.metadata.get("source", None) for doc, _score in results]

    content_start = response_text.find("content=")
    if content_start != -1:
        response_text = response_text[content_start + len("content="):]
    st.write(response_text)

    # Add to chat history
    add_to_chat_history(f'You: {query_text}')
    add_to_chat_history(f'Bot: {response_text}')

    current_position += 1
    new_query_key = f"new_query_{current_position}"  # Unique key based on the current position
    new_query = st.text_input(" ", key=new_query_key)
    if new_query:
        query_res(new_query, db, current_position)

# Function to initialize session state
def init_session_state():
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'current_position' not in st.session_state:
        st.session_state.current_position = 0

init_session_state()
# Function to add query to chat history
def add_to_chat_history(query):
    st.session_state.chat_history.append(query)

def display_chat_history():
    st.sidebar.subheader("Chat History")
    for item in st.session_state.chat_history:
        st.sidebar.text(item)

# Streamlit UI
display_chat_history()

# Load model and database
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    st.error("OpenAI API key not found. Please set it in the .env file.")

embedding_function = OpenAIEmbeddings(api_key=openai_api_key)
db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

user_query = st.text_input("Ask me something about Covid-19: ")

if user_query:
    # Generate response
    query_res(user_query, db, st.session_state.current_position)

st.cache_data.clear()
st.cache_resource.clear()
