import streamlit as st

from services.workspace_service import (
    save_project,
    load_project,
    get_projects
)


def show_workspace():

    st.title(
        "📂 Research Workspace"
    )

    st.write(
        """
Create and manage research projects.
        """
    )

    project_name = st.text_input(
        "Project Name"
    )

    research_topic = st.text_input(
        "Research Topic"
    )

    notes = st.text_area(
        "Project Notes",
        height=200
    )

    if st.button(
        "Save Project"
    ):

        if project_name:

            save_project(
                project_name,
                {
                    "topic": research_topic,
                    "notes": notes
                }
            )

            st.success(
                "Project saved successfully."
            )

        else:

            st.warning(
                "Enter a project name."
            )

    st.markdown("---")

    st.subheader(
        "Saved Projects"
    )

    projects = get_projects()

    if projects:

        selected_project = st.selectbox(
            "Select Project",
            projects
        )

        if st.button(
            "Open Project"
        ):

            project = load_project(
                selected_project
            )

            if project:

                st.write(
                    f"### {selected_project}"
                )

                st.write(
                    f"**Topic:** {project['topic']}"
                )

                st.write(
                    project["notes"]
                )

    else:

        st.info(
            "No saved projects yet."
        )