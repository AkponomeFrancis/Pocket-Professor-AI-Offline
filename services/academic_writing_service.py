from services.ai_service import ask_ai


def generate_academic_content(
    topic,
    level,
    content_type
):

    prompt = f"""
You are an expert academic writing assistant.

Research Topic:
{topic}

Academic Level:
{level}

Content Type:
{content_type}

Generate detailed academic content suitable for the selected level.

Requirements:

- Use formal academic language.
- Use proper headings and subheadings.
- Make the content detailed and well-structured.
- Ensure originality and clarity.

If Content Type is:

Research Proposal:
Include:
- Background of the Study
- Statement of the Problem
- Aim and Objectives
- Research Questions
- Significance of the Study
- Scope of the Study
- Proposed Methodology

Chapter 1:
Include:
- Background of the Study
- Statement of the Problem
- Aim and Objectives
- Research Questions
- Research Hypotheses (if applicable)
- Significance of the Study
- Scope of the Study
- Definition of Terms

Chapter 2:
Include:
- Conceptual Review
- Theoretical Framework
- Empirical Review
- Research Gap
- Summary

Chapter 3:
Include:
- Research Design
- Population of the Study
- Sample Size
- Sampling Technique
- Instrument for Data Collection
- Validity and Reliability
- Method of Data Collection
- Method of Data Analysis

Chapter 4:
Include:
- Data Presentation
- Data Analysis
- Discussion of Findings
- Interpretation of Results

Chapter 5:
Include:
- Summary
- Conclusion
- Recommendations
- Suggestions for Further Studies

Journal Article:
Include:
- Abstract
- Introduction
- Literature Review
- Methodology
- Results
- Discussion
- Conclusion
- References

Seminar Paper:
Include:
- Abstract
- Introduction
- Main Discussion
- Conclusion
- References

Conference Paper:
Include:
- Abstract
- Introduction
- Methodology
- Findings
- Conclusion
- References

Literature Review:
Include:
- Introduction
- Main Themes
- Key Findings
- Similarities
- Differences
- Research Gaps
- Conclusion
"""

    return ask_ai(prompt)