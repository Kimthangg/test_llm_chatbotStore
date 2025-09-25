from langchain_openai import ChatOpenAI

import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")
API_BASE="https://generativelanguage.googleapis.com/v1beta/openai/"
MODEL_NAME="gemini-2.0-flash"

#Khởi tạo llm
llm = ChatOpenAI(model_name=MODEL_NAME,
                 temperature=0,
                 openai_api_key=API_KEY,
                 openai_api_base=API_BASE)
# print(llm.invoke("Thủ đô việt nam là gì"))

from langchain_community.embeddings import GPT4AllEmbeddings
embedding_model = GPT4AllEmbeddings(model_file='all-MiniLM-L6-v2-f16.gguf')

# print(embedding_model.embed_query("Hello world"))