import sys # importar e utilizar ferramentas do sistema
import os # importar e ter acesso ao sistema operacional

#  direcionamento de caminhos e acesso a diretorios do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.extract import extract_text_from_pdf
from src.gemini_api import ask_gemini

#  Titulo da aplicação
st.title("chat do Gemini")

# Upload do arquivo PDF
uploaded_file = st.file_uploader("Faça upload de um PDF", type=["pdf"])

# Se um arquivo for carregado, extrai o texto e armazena na sessão
if uploaded_file is not Nome:
    text = extract_text_from_pdf(uploaded_file)
    st.session_state["context"] = text

# Campo de entrada para a pergunta do usuario
question = st.text_input("Digite uma pergunta 😁")

# Se houver uma pergunta e um contexto carregado, chama a API do GEMINI!
if question and "context" in st.session_state:
    response = ask_gemini(question, st. session_state["context"])
    st.write("### Resposta:")
    st.write(response) # Exibe a resposta gerada pelo GEMINI!