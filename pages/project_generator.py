import streamlit as st

from services.project_service import (
    generate_project_chapter
)

from services.pdf_export_service import (
    create_pdf
)


def show_project_generator():

    st.title(
        "📚 Research Project Generator"
    )

    st.write(
        """
Generate complete academic project sections,
including abstracts, chapters, references,
and appendices.
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

    section = st.selectbox(
        "Project Section",
        [
            "Abstract",
            "Table of Contents",
            "Chapter 1",
            "Chapter 2",
            "Chapter 3",
            "Chapter 4",
            "Chapter 5",
            "References",
            "Appendix"
        ]
    )

    if st.button(
        "Generate Project Section"
    ):

        if not topic.strip():

            st.warning(
                "Please enter a research topic."
            )

            return

        try:

            with st.spinner(
                "Generating project section..."
            ):

                content = generate_project_chapter(
                    topic,
                    level,
                    section
                )

            if not content:

                st.warning(
                    "No content was generated."
                )

                return

            if (
                "projects_generated"
                not in st.session_state
            ):
                st.session_state[
                    "projects_generated"
                ] = 0

            st.session_state[
                "projects_generated"
            ] += 1

            st.success(
                "Project section generated successfully."
            )

            st.write(content)

            pdf_file = create_pdf(
                content,
                section
            )

            with open(
                pdf_file,
                "rb"
            ) as file:

                st.download_button(
                    label="📄 Download PDF",
                    data=file,
                    file_name="project_section.pdf",
                    mime="application/pdf"
                )

        except Exception as e:

            st.error(
                f"Error: {str(e)}"
            )