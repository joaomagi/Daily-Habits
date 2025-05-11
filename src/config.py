from dotenv import load_dotenv  # Biblioteca para utilização do dotenv
import os # Biblioteca para interação com o sistema operacional, usada nesse caso para carregar variáveis de ambiente
from langchain_groq import ChatGroq # Biblioteca para utilização do grop

def ia_model():
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    if api_key is None:
        raise ValueError("A chave de API da Groq não foi encontrada. Verifique se o arquivo .env está configurado corretamente.")

    # Criação do modelo Groq, com definição do modelo, temperatura que define o nível de criatividade e limite máximo de tentativas caso falhe as requisições
    groq = ChatGroq(
        model="llama3-70b-8192",
        temperature=0.5,
        max_retries=2,
    )
    return groq