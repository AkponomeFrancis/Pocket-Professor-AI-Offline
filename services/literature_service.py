from services.ai_service import ask_ai


def generate_literature_review(text):

    prompt = f"""
You are an academic literature review assistant.

Based on the content provided, generate a structured literature review.

Include the following sections:

1. Main Themes
2. Key Findings
3. Similarities Among Studies
4. Differences Among Studies
5. Research Gaps
6. Recommendations for Future Research
7. Summary

Content:
{text}

Use formal academic language and clear headings.
"""

    return ask_ai(prompt)