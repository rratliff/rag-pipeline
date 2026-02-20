import logging
import os.path
import time
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
    Settings
)
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama

logging.basicConfig(level=logging.WARNING)

Settings.llm = Ollama(
    model="llama3",        # any model you have pulled
    request_timeout=120.0,
    base_url="http://localhost:11434"
)

Settings.embed_model = OllamaEmbedding(
    model_name="nomic-embed-text",
    base_url="http://localhost:11434"
)

start_time = time.time()

PERSIST_DIR = "./storage"
if not os.path.exists(PERSIST_DIR):
    print("load the documents and create the index in storage")
    documents = SimpleDirectoryReader("my_docs").load_data()
    index = VectorStoreIndex.from_documents(documents)
    # store it for later
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    print("storage directory found. Loading index from storage")
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)

end_time = time.time()
duration = end_time - start_time
print(f"Loading completed in {duration:.2f} seconds.")

query_engine = index.as_query_engine()

query = "What are some skills the author has for IT management?"
print(query)
response = query_engine.query(query)
print(response)

query = "What are some hard drive issues the author has experienced?"
print(query)
response = query_engine.query(query)
print(response)
