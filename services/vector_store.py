import os

# Force Hugging Face and Transformers to work offline
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


class VectorStore:
    """
    Offline vector database using:
    - Sentence Transformers for embeddings
    - FAISS for local similarity search

    No internet connection required after model download.
    """

    def __init__(self):

        print("Loading offline embedding model...")

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2",
            local_files_only=True
        )

        print("Embedding model loaded successfully.")

        self.index = None
        self.chunks = []


    def create_index(self, chunks):
        """
        Convert document chunks into embeddings
        and store them locally using FAISS.
        """

        if not chunks:
            raise ValueError(
                "No document chunks provided."
            )

        self.chunks = chunks

        print("Creating document embeddings...")

        embeddings = self.model.encode(
            chunks,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        dimension = embeddings.shape[1]

        # FAISS local index
        self.index = faiss.IndexFlatIP(
            dimension
        )

        self.index.add(
            embeddings
        )

        print(
            f"Vector index created with {len(chunks)} chunks."
        )


    def search(self, query, top_k=3):
        """
        Search the local FAISS database
        and return the most relevant chunks.
        """

        if self.index is None:
            return []


        query_embedding = self.model.encode(
            [query],
            convert_to_numpy=True,
            normalize_embeddings=True
        )


        distances, indices = self.index.search(
            query_embedding,
            top_k
        )


        results = []

        for idx in indices[0]:

            if idx < len(self.chunks):
                results.append(
                    self.chunks[idx]
                )


        return results