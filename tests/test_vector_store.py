from services.chunking import chunk_text
from services.vector_store import VectorStore


sample_text = """
Artificial Intelligence is a branch of computer science.

Machine Learning is a subset of Artificial Intelligence.

Deep Learning is a subset of Machine Learning.

Neural Networks are commonly used in Deep Learning.
"""


chunks = chunk_text(sample_text)

store = VectorStore()

store.create_index(chunks)

results = store.search(
    "What is Machine Learning?"
)

print("\nResults:\n")

for result in results:

    print(result)