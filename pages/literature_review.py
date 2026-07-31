import streamlit as st

from services.pdf_service import (
    extract_text_from_pdf
)

from services.literature_service import (
    generate_literature_review
)

from services.pdf_export_service import (
    create_pdf
)


def show_literature_review():

    st.title("📖 Literature Review Assistant")

    st.write(
        """
Upload a research paper and generate a structured
literature review automatically.
        """
    )

    uploaded_file = st.file_uploader(
        "Upload a Research Paper",
        type=["pdf"]
    )

    if not uploaded_file:

        st.info(
            "Upload a research paper to begin."
        )

        return

    try:

        if uploaded_file.name != st.session_state.literature_file:

            with st.spinner(
                "Reading research paper..."
            ):

                text = extract_text_from_pdf(
                    uploaded_file
                )

                st.session_state.literature_text = (
                    text[:5000]
                )

                st.session_state.literature_file = (
                    uploaded_file.name
                )

            st.success(
                "Research paper loaded successfully."
            )

        if st.button(
            "Generate Literature Review"
        ):

            if not st.session_state.literature_text:

                st.warning(
                    "No document content available."
                )

                return

            with st.spinner(
                "Analyzing paper and generating literature review..."
            ):

                review = generate_literature_review(
                    st.session_state.literature_text
                )

            if not review:

                st.warning(
                    "No literature review was generated."
                )

                return

            st.session_state.literature_reviews_generated += 1

            st.success(
                "Literature review generated successfully."
            )

            st.markdown(
                "### Literature Review"
            )

            st.write(review)

            pdf_file = create_pdf(
                review,
                "Literature Review"
            )

            with open(
                pdf_file,
                "rb"
            ) as file:

                st.download_button(
                    label="📄 Download Literature Review PDF",
                    data=file,
                    file_name="literature_review.pdf",
                    mime="application/pdf"
                )

    except Exception as e:

        st.error(
            f"Error generating literature review: {str(e)}"
        )