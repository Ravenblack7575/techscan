'''
This file contains configuration for LLMs and embeddings.
To use the objects in this module, do an import just like you would if you are importing a library ("from config import ...").
If api keys are required, this module will load them from a .env file in the same folder as this config.py file.
Make sure you have a .env file with the correct keys in the same folder as this config.py file.
'''

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

#Always load .env from the same folder as this config.py
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

# load_dotenv()



# Local LLM
llm_local = ChatOpenAI(
    api_key="NIL",
    openai_api_base="http://localhost:1234/v1/",
)

# Openrouter LLM
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
llm_open_router = ChatOpenAI(
    api_key=OPENROUTER_API_KEY,
    openai_api_base="https://openrouter.ai/api/v1/",
    model="mistralai/mistral-small-3.2-24b-instruct-2506:free",
)


# # langchain embeddings using HuggingFace (check this because it changes often)
# from langchain.embeddings import HuggingFaceEmbeddings
# hf_embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2")




'''Other services, unccomment if needed.'''

#serpapi key for google search
SERPAPI_API_KEY = os.environ.get("SERPAPI_API_KEY")


# Optional: For Deepseek API
# DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API")
# llm_deepseek = ChatDeepSeek(model="...",temperature=0,max_tokens=None,timeout=None,max_retries=2,api_key=DEEPSEEK_API_KEY)

# Optional: For those running with Ollama
# from langchain_community.chat_models import ChatOllama
# from langchain_ollama import ChatOllama
# llm_ollama = ChatOllama(model="llama3")

# Optional: For those with OpenAIAPI
# OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
# llm_openai = ChatOpenAI(
#     openai_api_key=OPENAI_API_KEY,
# )

# # Postgres connection string
# DATABASE_URL = os.environ.get("DATABASE_URL")


