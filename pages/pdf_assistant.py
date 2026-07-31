import streamlit as st

from services.pdf_service import extract_text_from_pdf

from services.rag_service import (
    index_document,
    ask_pdf
)


def show_pdf_assistant():

    st.title("📄 PDF Assistant")

    st.write(
        "Upload a PDF and ask questions directly from its content."
    )

    uploaded_file = st.file_uploader(
        "Upload a PDF",
        type=["pdf"]
    )

    if not uploaded_file:

        st.info(
            "Upload a PDF to begin."
        )

        return

    try:

        if uploaded_file.name != st.session_state.current_pdf:

            with st.spinner(
                "Reading and indexing PDF..."
            ):

                text = extract_text_from_pdf(
                    uploaded_file
                )

                text = text[:15000]

                index_document(text)

                st.session_state.current_pdf = (
                    uploaded_file.name
                )

                st.session_state.pdf_uploads += 1

            st.success(
                "PDF indexed successfully."
            )

        question = st.text_input(
            "Ask a question about the PDF"
        )

        if st.button(
            "Get PDF Answer"
        ):

            if not question.strip():

                st.warning(
                    "Please enter a question."
                )

                return

            with st.spinner(
                "Searching document..."
            ):

                answer = ask_pdf(
                    question
                )

            st.success(
                "Answer generated successfully."
            )

            st.write(answer)

    except Exception as e:

        st.error(
            f"PDF processing error: {str(e)}"
        )