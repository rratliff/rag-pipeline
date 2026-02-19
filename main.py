import logging

logging.basicConfig(level=logging.WARNING)

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
from llama_index.llms.ollama import Ollama

Settings.llm = Ollama(
    model="llama3",        # any model you have pulled
    request_timeout=120.0,
    base_url="http://localhost:11434"
)

documents = SimpleDirectoryReader("my_docs").load_data()
index = VectorStoreIndex.from_documents(documents, embed_model=HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5"))
query_engine = index.as_query_engine()
response = query_engine.query("What are some skills the author has for IT management?")
print(response)

