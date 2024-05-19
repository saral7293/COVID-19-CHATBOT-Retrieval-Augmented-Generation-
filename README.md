## About
This repository contains a Chatbot application built using Streamlit, LangChain, and ChromaDB, designed to provide important information about COVID-19 based on the contents of PDF files. The chatbot utilizes a Retrieval-Augmented-Generation (RAG) approach, where relevant information is retrieved from a vector database and then processed by a language model to generate a final answer.
## Table of Contents
* [Features](#features)
* [Architecture](#architecture)
* [Installation](#installation)
* [Usage](#usage)
* [Deployment](#deployment)
* [Contribution](#contribution)
* [FutureWork](#futurework)
## Features
1. PDF Ingestion: The chatbot can ingest PDF files containing COVID-19 related information and create a vector database using ChromaDB.
2. Question Answering: Users can ask questions related to COVID-19, and the chatbot will retrieve relevant information from the vector database and generate a response using a language model.
3. Streamlit Interface: The chatbot has a user-friendly interface built with Streamlit, allowing users to interact with the application through a web-based interface.
## Architecture
The chatbot follows a Retrieval-Augmented-Generation (RAG) approach, which combines retrieval and generation techniques to provide accurate and relevant answers. The architecture consists of the following components:
1. Document Loader: Loads PDF files from the Books folder and splits them into smaller text chunks.
2. Vector Database: The text chunks are converted into vector embeddings using OpenAI's embeddings and stored in a ChromaDB vector database.
3. Similarity Search: When a user asks a question, relevant text chunks are retrieved from the vector database based on their similarity to the question.
4. Language Model: The retrieved text chunks are passed to a language model (GPT-3.5-turbo) along with the user's question. The model generates a final answer based on the provided context.
5. Streamlit Interface: The user interface is built using Streamlit, allowing users to interact with the chatbot through a web-based interface.
## Installation
1. Clone the repositry:
```
git clone https://github.com/saral7293/COVID-19-CHATBOT-Retrieval-Augmented-Generation-
```
2. Navigate to the project directory:
```
cd COVID-19-CHATBOT-Retrieval-Augmented-Generation
```
3. Install the required dependencies:
```
pip install -r requirements.txt
```
4. Set your OpenAI API key as an environment variable:
```
export OPENAI_API_KEY=your_openai_api_key
```
## Usage
To run the chatbot locally using Streamlit, execute the following command:
```
streamlit run app.py
```
This will start the Streamlit application, and you can interact with the chatbot through the web interface.
## Deployment
This chatbot has been deployed on an EC2 instance in a VM.
## Contribution
Contributions are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request.
## FutureWork
Fine tune the chatbot and apply Advance RAG techniques.

