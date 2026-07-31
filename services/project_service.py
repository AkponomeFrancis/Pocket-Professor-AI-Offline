from services.ai_service import ask_ai


def generate_project_chapter(
    topic,
    level,
    section
):

    prompt = f"""
You are an expert academic research supervisor.

Research Topic:
{topic}

Academic Level:
{level}

Project Section:
{section}

Generate detailed academic content suitable for the selected academic level.

Instructions:

- Use proper academic formatting.
- Use headings and subheadings.
- Be detailed and professional.
- Use scholarly writing style.

Section Requirements:

ABSTRACT
Include:
- Background
- Objective
- Methodology
- Findings
- Conclusion
- Keywords

TABLE OF CONTENTS
Include:
- Title Page
- Certification
- Approval Page
- Dedication
- Acknowledgements
- Abstract
- Table of Contents
- Chapter One
- Chapter Two
- Chapter Three
- Chapter Four
- Chapter Five
- References
- Appendices

CHAPTER 1
Include:
- Background of the Study
- Statement of the Problem
- Aim and Objectives
- Research Questions
- Research Hypotheses
- Significance of the Study
- Scope of the Study
- Definition of Terms

CHAPTER 2
Include:
- Conceptual Review
- Theoretical Framework
- Empirical Review
- Research Gap
- Summary of Literature Review

CHAPTER 3
Include:
- Research Design
- Population of the Study
- Sample Size
- Sampling Technique
- Instrument for Data Collection
- Validity and Reliability
- Method of Data Collection
- Method of Data Analysis

CHAPTER 4
Include:
- Data Presentation
- Data Analysis
- Discussion of Findings
- Interpretation of Results

CHAPTER 5
Include:
- Summary
- Conclusion
- Recommendations
- Suggestions for Further Studies

REFERENCES
Generate at least 20 APA 7th Edition references.

APPENDIX
Generate:
- Questionnaire
- Interview Guide
- Consent Form

Generate the requested section now.
"""

    return ask_ai(prompt)