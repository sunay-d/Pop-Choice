from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def get_embedding(text):
    try:
        return model.encode(text, normalize_embeddings=True).tolist()
    except Exception as e:
        print(e)
        return []

def get_list_embeddings(input_text_list):
    try:
        embeddings = []
        for input_text in input_text_list:
            embedding = get_embedding(input_text)
            embeddings.append({
                "content": input_text,
                "embedding": embedding
            })
        return embeddings
    except Exception as e:
        print(e)
        return []
