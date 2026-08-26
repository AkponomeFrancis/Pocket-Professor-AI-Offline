from pathlib import Path

from llama_cpp import Llama


# Path to the local GGUF model
MODEL_PATH = (
    Path(__file__).resolve().parent.parent
    / "model"
    / "Llama-3.2-3B-Instruct-Q4_K_M.gguf"
)


# Load the model once when the service starts
llm = Llama(
    model_path=str(MODEL_PATH),
    n_ctx=2048,
    n_threads=4,
    verbose=False,
)


def ask_ai(prompt):
    """Generate a response using the local GGUF model."""

    print("Sending question to local llama.cpp...")

    response = llm.create_chat_completion(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        max_tokens=512,
        temperature=0.7,
    )

    print("Response received from local model.")

    return response["choices"][0]["message"]["content"]