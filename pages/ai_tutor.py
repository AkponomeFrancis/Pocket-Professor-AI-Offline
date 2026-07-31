import streamlit as st

from services.ai_service import ask_ai


def show_ai_tutor():

    st.title("🤖 AI Tutor")

    st.write(
        "Ask any academic question and receive an AI-powered explanation."
    )

    question = st.text_area(
        "Ask a Question",
        height=150
    )

    if st.button("Get Answer"):

        if not question.strip():

            st.warning(
                "Please enter a question."
            )

            return

        try:

            with st.spinner("Thinking..."):

                answer = ask_ai(question)

            st.session_state.ai_questions += 1

            st.success(
                "Answer generated successfully."
            )

            st.write(answer)

        except Exception as e:

            st.error(
                f"Error generating answer: {str(e)}"
            )