from services.rag_service import ask_pdf


def generate_notes():

    prompt = """
You are an academic note-taking assistant.

Using the uploaded document, generate well-organized study notes.

Include the following sections:

1. Main Topics
2. Key Concepts
3. Important Points
4. Definitions (if available)
5. Summary

Use clear headings and bullet points where appropriate.

Make the notes easy for students to revise and study.
"""

    return ask_pdf(prompt)