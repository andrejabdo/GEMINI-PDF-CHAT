import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os 

load_dotenv()

# Configuração da chave da API
GOOGLE_GEMINI_API_KEY = os.getenv("GOOGLE_GEMINI_API_KEY")
if not GOOGLE_GEMINI_API_KEY:
    st.error("Defina a variável de ambiente GOOGLE_GEMINI_API_KEY")
    st.stop()

genai.configure(api_key=GOOGLE_GEMINI_API_KEY)

# Criar modelo
mode = genai.GenerativeModel("gemini-1.0-pro")

# Interface do Streamlit
st.set_page_config(page_title="Chat com IA Generativa", page_icon="🧑‍🔧", layout="wide")

# Adicionando plano de fundo personalizado
st.markdown(
    """
    <style>
        body {
            background-image: url('https://via.placeholder.com/1200x800');
            background-size: cover; 
            background-position: center;
            background-attachment: fixed;
            color: white;
        }
        .stapp{
        blackground-color: rgba(0, 0, 0,0.6);
        padding-radius: 10px;
        }

    </style>
    """,
    unsafe_allow_html=True
)

# Carregar e exibir imagem do assistente
image = Image.open("assistente.png")
st.image(image, width=150)

st.title("Assistente de IA Generativa")

prompt = st.text_input("Digite sua pergunta:")
if st.button("Gerar Resposta"):
    if prompt:
        response = mode.generate_content(prompt)
        st.write(response.text)
    else:
        st.warning("Por favor, insira um prompt.")