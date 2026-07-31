import json
import os


PROJECT_FOLDER = "data/projects"


def save_project(
    project_name,
    project_data
):

    os.makedirs(
        PROJECT_FOLDER,
        exist_ok=True
    )

    file_path = os.path.join(
        PROJECT_FOLDER,
        f"{project_name}.json"
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            project_data,
            file,
            indent=4
        )


def load_project(
    project_name
):

    file_path = os.path.join(
        PROJECT_FOLDER,
        f"{project_name}.json"
    )

    if not os.path.exists(
        file_path
    ):

        return None

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(
            file
        )


def get_projects():

    os.makedirs(
        PROJECT_FOLDER,
        exist_ok=True
    )

    projects = []

    for file in os.listdir(
        PROJECT_FOLDER
    ):

        if file.endswith(
            ".json"
        ):

            projects.append(
                file.replace(
                    ".json",
                    ""
                )
            )

    return projects