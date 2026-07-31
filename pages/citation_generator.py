import streamlit as st

from services.citation_service import (
    generate_citation
)

from services.pdf_export_service import (
    create_pdf
)


def show_citation_generator():

    st.title("📚 Citation Generator")

    st.write(
        """
Generate academic citations in multiple citation styles.
        """
    )

    author = st.text_input(
        "Author"
    )

    title = st.text_input(
        "Title"
    )

    year = st.text_input(
        "Year"
    )

    publisher = st.text_input(
        "Publisher"
    )

    style = st.selectbox(
        "Citation Style",
        [
            "APA 7th",
            "MLA 9th",
            "Harvard",
            "Chicago"
        ]
    )

    if st.button(
        "Generate Citation"
    ):

        if not all([
            author.strip(),
            title.strip(),
            year.strip(),
            publisher.strip()
        ]):

            st.warning(
                "Please complete all fields."
            )

            return

        try:

            with st.spinner(
                "Generating citation..."
            ):

                citation = generate_citation(
                    author,
                    title,
                    year,
                    publisher,
                    style
                )

            if not citation:

                st.warning(
                    "No citation was generated."
                )

                return

            st.session_state.citations_generated += 1

            st.success(
                "Citation generated successfully."
            )

            st.markdown(
                "### Generated Citation"
            )

            st.code(
                citation,
                language=None
            )

            pdf_file = create_pdf(
                citation,
                "Citation"
            )

            with open(
                pdf_file,
                "rb"
            ) as file:

                st.download_button(
                    label="📄 Download Citation PDF",
                    data=file,
                    file_name="citation.pdf",
                    mime="application/pdf"
                )

        except Exception as e:

            st.error(
                f"Error generating citation: {str(e)}"
            )