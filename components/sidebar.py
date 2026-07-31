import streamlit as st


def show_sidebar():

    st.sidebar.title(
        "🎓 Pocket Professor AI"
    )

    st.sidebar.markdown(
        "---"
    )

    page = st.sidebar.radio(
        "Navigation",
        [
            "Dashboard",
            "About",
            "AI Tutor",
            "PDF Assistant",
            "Notes Generator",
            "Research Ideas",
            "Citation Generator",
            "Literature Review",
            "Research Gap Finder",
            "Academic Writing Assistant",
            "Research Project Generator",
            "Research Workspace"
            
        ]
    )

    st.sidebar.markdown(
        "---"
    )

    st.sidebar.info(
        "Offline Educational AI for Students and Researchers"
    )

    return page