import os

# Force offline operation
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

from ollama import chat

from services.chunking import chunk_text
from services.vector_store import VectorStore


# Initialize local vector database
vector_store = VectorStore()


def index_document(text):
    """
    Process uploaded document text,
    split into chunks, and create
    a local FAISS index.
    """

    if not text:
        raise ValueError(
            "No document text provided."
        )

    print("Splitting document into chunks...")

    chunks = chunk_text(text)

    print(
        f"Created {len(chunks)} chunks."
    )

    vector_store.create_index(
        chunks
    )

    print(
        "Document indexed successfully."
    )


def ask_pdf(question):
    """
    Answer questions using:
    - Local FAISS retrieval
    - Local Sentence Transformer embeddings
    - Local Ollama LLM

    No internet required.
    """

    if vector_store.index is None:

        return """
Please upload and index a PDF first.

Steps:

1. Open PDF Assistant
2. Upload a PDF
3. Wait for indexing
4. Ask your question
"""


    try:

        print(
            "Searching document..."
        )

        context_chunks = vector_store.search(
            question,
            top_k=3
        )


        if not context_chunks:

            return """
No relevant information was found
in the uploaded PDF.

Try asking the question differently.
"""


        context = "\n\n".join(
            context_chunks
        )


        prompt = f"""
You are Pocket Professor AI,
an offline academic assistant.

Use ONLY the information provided
in the context below.

If the answer is not available,
say:

"I could not find this information
in the uploaded document."

Context:

{context}


Question:

{question}
"""


        print(
            "Generating answer locally..."
        )


        response = chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )


        return response["message"]["content"]


    except Exception as e:

        print(
            f"RAG error: {e}"
        )

        return (
            "An error occurred while "
            f"processing your request: {str(e)}"
        )