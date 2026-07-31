from ollama import chat


def ask_ai(prompt):

    print("Sending question to Ollama...")

    response = chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print("Response received.")

    return response["message"]["content"]