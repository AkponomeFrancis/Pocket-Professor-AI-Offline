from services.ai_service import ask_ai


def find_research_gaps(topic_area, level):

    prompt = f"""
You are an academic research advisor.

Research Area:
{topic_area}

Academic Level:
{level}

Identify the following:

1. Five important research gaps
2. Why each gap is important
3. A possible research topic for each gap
4. Suggested future research directions
5. Potential practical impact of addressing each gap

Ensure the recommendations are:
- Relevant
- Current
- Academic
- Suitable for the selected level

Use clear headings and numbering.
"""

    return ask_ai(prompt)