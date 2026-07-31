import streamlit as st

from services.academic_writing_service import (
    generate_academic_content
)

from services.pdf_export_service import (
    create_pdf
)


def show_academic_writing():

    st.title("✍️ Academic Writing Assistant")

    st.write(
        """
Generate academic content for research,
projects, seminars, journal articles,
and academic writing tasks.
        """
    )

    topic = st.text_input(
        "Research Topic"
    )

    level = st.selectbox(
        "Academic Level",
        [
            "Secondary School",
            "Undergraduate",
            "Master's",
            "PhD"
        ]
    )

    content_type = st.selectbox(
        "Content Type",
        [
            "Research Proposal",
            "Chapter 1",
            "Chapter 2",
            "Chapter 3",
            "Chapter 4",
            "Chapter 5",
            "Journal Article",
            "Seminar Paper",
            "Conference Paper",
            "Literature Review"
        ]
    )

    if st.button(
        "Generate Academic Content"
    ):

        if not topic.strip():

            st.warning(
                "Please enter a research topic."
            )

            return

        try:

            with st.spinner(
                "Generating academic content..."
            ):

                content = generate_academic_content(
                    topic,
                    level,
                    content_type
                )

            if not content:

                st.warning(
                    "No content was generated."
                )

                return

            if (
                "academic_contents_generated"
                not in st.session_state
            ):
                st.session_state[
                    "academic_contents_generated"
                ] = 0

            st.session_state[
                "academic_contents_generated"
            ] += 1

            st.success(
                "Academic content generated successfully."
            )

            st.write(content)

            pdf_file = create_pdf(
                content,
                content_type
            )

            with open(
                pdf_file,
                "rb"
            ) as file:

                st.download_button(
                    label="📄 Download PDF",
                    data=file,
                    file_name="academic_content.pdf",
                    mime="application/pdf"
                )

        except Exception as e:

            st.error(
                f"Error: {str(e)}"
            )