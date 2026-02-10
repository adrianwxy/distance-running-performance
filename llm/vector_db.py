
import chromadb
from chromadb.utils import embedding_functions

def get_collection(path: str):
    client = chromadb.PersistentClient(path=path)

    embedding_f = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="BAAI/bge-large-en-v1.5",
        device="cpu"
    )

    return client.get_or_create_collection(
        name="analysis_outcomes",
        embedding_function=embedding_f
    )
