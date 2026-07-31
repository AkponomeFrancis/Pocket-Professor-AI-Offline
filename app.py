import streamlit as st

from config import APP_NAME

from components.sidebar import show_sidebar
from components.footer import show_footer

from pages.dashboard import show_dashboard
from pages.about import show_about
from pages.ai_tutor import show_ai_tutor
from pages.pdf_assistant import show_pdf_assistant
from pages.notes_generator import show_notes_generator
from pages.research_ideas import show_research_ideas
from pages.citation_generator import show_citation_generator
from pages.literature_review import show_literature_review
from pages.research_gap_finder import show_research_gap_finder
from pages.academic_writing import show_academic_writing
from pages.project_generator import show_project_generator
from pages.workspace import show_workspace



def load_css():
    try:
        with open("assets/style.css", "r", encoding="utf-8") as file:
            st.markdown(
                f"<style>{file.read()}</style>",
                unsafe_allow_html=True
            )
    except FileNotFoundError:
        pass


def initialize_session_state():

    defaults = {
        "ai_questions": 0,
        "pdf_uploads": 0,
        "notes_generated": 0,
        "research_ideas_generated": 0,
        "citations_generated": 0,
        "literature_reviews_generated": 0,
        "research_gaps_generated": 0,
        "projects_generated": 0,
        "current_pdf": "",
        "literature_file": "",
        "literature_text": ""
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


st.set_page_config(
    page_title=APP_NAME,
    page_icon="🎓",
    layout="wide"
)

initialize_session_state()
load_css()

page = show_sidebar()

if page == "Dashboard":
    show_dashboard()

elif page == "About":
    show_about()

elif page == "AI Tutor":
    show_ai_tutor()

elif page == "PDF Assistant":
    show_pdf_assistant()

elif page == "Notes Generator":
    show_notes_generator()

elif page == "Research Ideas":
    show_research_ideas()

elif page == "Citation Generator":
    show_citation_generator()

elif page == "Literature Review":
    show_literature_review()

elif page == "Research Gap Finder":
    show_research_gap_finder()

elif page == "Academic Writing Assistant":
    show_academic_writing()

elif page == "Research Project Generator":
    show_project_generator()

elif page == "Research Workspace":
    show_workspace()

show_footer()