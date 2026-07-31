import streamlit as st

from services.research_service import (
    generate_research_ideas
)

from services.pdf_export_service import (
    create_pdf
)


def show_research_ideas():

    st.title("💡 Research Ideas Generator")

    st.write(
        """
Generate innovative research topics based on your area of interest
and academic level.
        """
    )

    topic_area = st.text_input(
        "Enter a Research Area"
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

    if st.button(
        "Generate Research Ideas"
    ):

        if not topic_area.strip():

            st.warning(
                "Please enter a research area."
            )

            return

        try:

            with st.spinner(
                "Generating research ideas..."
            ):

                ideas = generate_research_ideas(
                    topic_area,
                    level
                )

            if not ideas:

                st.warning(
                    "No research ideas were generated."
                )

                return

            st.session_state.research_ideas_generated += 1

            st.success(
                "Research ideas generated successfully."
            )

            st.markdown(
                "### Research Ideas"
            )

            st.write(ideas)

            pdf_file = create_pdf(
                ideas,
                "Research Ideas"
            )

            with open(
                pdf_file,
                "rb"
            ) as file:

                st.download_button(
                    label="📄 Download Research Ideas PDF",
                    data=file,
                    file_name="research_ideas.pdf",
                    mime="application/pdf"
                )

        except Exception as e:

            st.error(
                f"Error generating research ideas: {str(e)}"
            )