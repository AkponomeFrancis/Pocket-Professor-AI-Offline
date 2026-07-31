def generate_citation(
    author,
    title,
    year,
    publisher,
    style
):

    if style == "APA 7th":

        return (
            f"{author} ({year}). "
            f"{title}. {publisher}."
        )

    elif style == "MLA 9th":

        return (
            f"{author}. "
            f"{title}. "
            f"{publisher}, {year}."
        )

    elif style == "Harvard":

        return (
            f"{author} ({year}) "
            f"{title}. "
            f"{publisher}."
        )

    elif style == "Chicago":

        return (
            f"{author}. "
            f"{title}. "
            f"{publisher}, {year}."
        )

    else:

        return "Citation style not supported."