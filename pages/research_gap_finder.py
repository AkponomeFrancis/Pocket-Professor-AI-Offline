import streamlit as st

from services.research_gap_service import (
    find_research_gaps
)

from services.pdf_export_service import (
    create_pdf
)


def show_research_gap_finder():

    st.title("🔍 Research Gap Finder")

    st.write(
        """
Discover research gaps, emerging opportunities,
and future research directions in your field of study.
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
        "Find Research Gaps"
    ):

        if not topic_area.strip():

            st.warning(
                "Please enter a research area."
            )

            return

        try:

            with st.spinner(
                "Analyzing research area..."
            ):

                gaps = find_research_gaps(
                    topic_area,
                    level
                )

            if not gaps:

                st.warning(
                    "No research gaps were identified."
                )

                return

            st.session_state.research_gaps_generated += 1

            st.success(
                "Research gaps identified successfully."
            )

            st.markdown(
                "### Research Gaps and Opportunities"
            )

            st.write(gaps)

            st.download_button(
                label="📥 Download as TXT",
                data=gaps,
                file_name="research_gaps.txt",
                mime="text/plain"
            )

            pdf_file = create_pdf(
                gaps,
                "Research Gaps"
            )

            with open(
                pdf_file,
                "rb"
            ) as file:

                st.download_button(
                    label="📄 Download as PDF",
                    data=file,
                    file_name="research_gaps.pdf",
                    mime="application/pdf"
                )

        except Exception as e:

            st.error(
                f"Error identifying research gaps: {str(e)}"
            )