import streamlit as st

from services.notes_service import generate_notes
from services.pdf_export_service import create_pdf


def show_notes_generator():

    st.title("📝 Notes Generator")

    st.write(
        """
Generate structured study notes from the PDF currently loaded
in the PDF Assistant.
        """
    )

    st.info(
        """
Before generating notes:

1. Open PDF Assistant
2. Upload a PDF
3. Wait for indexing to complete
4. Return here and generate notes
        """
    )

    if st.button(
        "Generate Notes"
    ):

        try:

            with st.spinner(
                "Analyzing document and generating notes..."
            ):

                notes = generate_notes()

            if not notes:

                st.warning(
                    "No notes were generated."
                )

                return

            st.session_state.notes_generated += 1

            st.success(
                "Notes generated successfully."
            )

            st.markdown("### Generated Notes")

            st.write(notes)

            pdf_file = create_pdf(
                notes,
                "Study Notes"
            )

            with open(
                pdf_file,
                "rb"
            ) as file:

                st.download_button(
                    label="📄 Download Notes PDF",
                    data=file,
                    file_name="study_notes.pdf",
                    mime="application/pdf"
                )

        except Exception as e:

            st.error(
                f"Error generating notes: {str(e)}"
            )