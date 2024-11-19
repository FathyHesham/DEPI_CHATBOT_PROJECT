import chromadb
import json
from sklearn.metrics.pairwise import cosine_similarity
from Embedding_Code import MyEmbeddingFunction
import numpy as np

def chromadatabase(query):
    try:
        with open('Dataset.json', 'r', encoding='utf-8') as file:
            all_text = json.load(file)
    except Exception as e:
        print(f"Error loading dataset: {e}")
        exit()

    corpus = all_text.get("all_text", [])

    # Instantiate the embedding function
    embedding_fn = MyEmbeddingFunction()

    # Generate embeddings for the corpus
    embeddings = embedding_fn(corpus)


    # Initialize the ChromaDB client
    client = chromadb.PersistentClient(path="Database/")

    # Create a new Chroma collection
    collection = client.get_or_create_collection(
        name="arabert_embeddings", 
        embedding_function=MyEmbeddingFunction()  # Use the custom embedding function
    )

    # Generate unique IDs for each document in the corpus
    ids = [str(i) for i in range(len(corpus))]

    # Insert the documents and their embeddings into the collection
    collection.upsert(documents=corpus, embeddings=embeddings, ids=ids)

    # Prompt the user to enter a query
    #query = input("Please Enter The Query: ")

    # Generate an embedding for the user's query
    embedding_query = embedding_fn(query)

    # Reshape embedding_query to ensure it is 2D
    embedding_query = np.array(embedding_query).reshape(1, -1)

    # Use cosine_similarity to calculate similarity between the query and the documents
    similarities = cosine_similarity(embedding_query, embeddings)

    # Get the index of the most similar document
    most_similar_idx = similarities.argmax()

    # Retrieve the most similar document
    most_similar_document = corpus[most_similar_idx]
    #print(f"الاجابة: {most_similar_document}")
    #print(f"Similarity Score: {similarities[0][most_similar_idx]}")

    return most_similar_document

