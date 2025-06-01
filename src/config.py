from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

def ia_model():
    """Configura e retorna o modelo ChatGroq pronto para uso"""
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    if api_key is None:
        raise ValueError("A chave de API da Groq não foi encontrada. Verifique se o arquivo .env está configurado corretamente.")

    groq = ChatGroq(
        model="llama3-70b-8192",
        temperature=0.5,
        max_retries=2,
    )
    return groq