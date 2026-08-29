import faiss
import numpy as np


def create_index(embeddings):
    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings).astype("float32"))

    return index
def search_index(query_embedding, index, chunks, k=1):

    query_embedding = np.array([query_embedding]).astype("float32")

    distances, indices = index.search(query_embedding, len(chunks))
    

    

    results = []

    for i in indices[0]:
        results.append(chunks[i])

    return results