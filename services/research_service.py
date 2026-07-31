from services.ai_service import ask_ai


def generate_research_ideas(topic_area, level):

    prompt = f"""
You are an academic research advisor.

Research Area:
{topic_area}

Academic Level:
{level}

Generate:

1. Five research topic ideas
2. Research problem for each topic
3. One objective for each topic
4. One research question for each topic

Make the ideas practical, relevant, and suitable for the selected academic level.
"""

    return ask_ai(prompt)