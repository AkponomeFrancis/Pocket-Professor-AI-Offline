from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import tempfile


def create_pdf(content, title):

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    )

    doc = SimpleDocTemplate(
        temp_file.name
    )

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(title, styles["Title"])
    )

    story.append(
        Spacer(1, 12)
    )

    for line in content.split("\n"):

        story.append(
            Paragraph(line, styles["BodyText"])
        )

    doc.build(story)

    return temp_file.name