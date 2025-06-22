from supabase import create_client, Client
from dotenv import load_dotenv
from .get_embedding import get_embedding, get_list_embeddings
from .content_splitter import content_in_chunks
import os

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def store_embeddings():
    embedding_list = get_list_embeddings(content_in_chunks)
    try:
        supabase.table("documents").insert(embedding_list).execute()
    except Exception as e:
        print(e)
        return "There was an error while stroing embeddings."
    
def search_similar(query, top_k=1, similarity=0.25):
    try:
        query_embedding = get_embedding(query)
        query_result = supabase.rpc(
            "match_documents",
            {
                "query_embedding": query_embedding,
                "match_threshold": similarity,
                "match_count": top_k
            }
        ).execute()

        if query_result.data:
            return query_result.data[0]["content"]
        else:
            return "No answer found."
    except Exception as e:
        print(e)
        return "There was an error while retrieving the answer."

#store_embeddings()