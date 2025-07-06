# Automated-Resume-Parser
CODTECH Internship Project 2 - Automated Resume Parser
This project extracts key information from a resume PDF using:
- **pdfplumber** (for PDF text extraction)
- **spaCy** (for name/entity recognition)
- **Regex** (for emails, phone, skills)

**Run:**
1. `pip install pdfplumber spacy`
2. `python -m spacy download en_core_web_sm`
3. `python resume_parser.py`
