import numpy as np  # Ensure NumPy is imported

# Initialize the SentenceTransformer model
from sentence_transformers import SentenceTransformer
from chromadb import EmbeddingFunction, Embeddings

model = SentenceTransformer("AbderrahmanSkiredj1/Arabic_text_embedding_for_sts")

# Create a custom embedding function by subclassing EmbeddingFunction
class MyEmbeddingFunction(EmbeddingFunction):
    def __call__(self, *args, **kwargs) -> Embeddings:
        input = args[0]  # Extract the input from args
        embeddings = model.encode(input, convert_to_numpy=True)  # Generate embeddings using the model
        return embeddings  # Return embeddings directly as a NumPy array