# resume_parser.py

"""
CODTECH Internship Project 2
Automated Resume Parser

This script extracts name, email, phone, education, and skills
from a resume PDF using pdfplumber and spaCy.
"""

import pdfplumber
import spacy
import re

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# 📌 Replace this with your PDF path
PDF_PATH = "sample_resume.pdf"

# Extract text from PDF
with pdfplumber.open(PDF_PATH) as pdf:
    pages = [page.extract_text() for page in pdf.pages]
    resume_text = "\n".join(pages)

# Process text with spaCy
doc = nlp(resume_text)

# Extract name (first PERSON entity)
name = None
for ent in doc.ents:
    if ent.label_ == "PERSON":
        name = ent.text
        break

# Extract email using regex
email = None
email_match = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", resume_text)
if email_match:
    email = email_match[0]

# Extract phone number using regex
phone = None
phone_match = re.findall(r"\+?\d[\d\s\-]{8,}\d", resume_text)
if phone_match:
    phone = phone_match[0]

# Extract education (simple keyword search)
education = None
if "Education" in resume_text:
    education_match = re.findall(r"Education:?\s*(.*)", resume_text)
    if education_match:
        education = education_match[0]

# Extract skills (simple keyword search)
skills = None
if "Skills" in resume_text:
    skills_match = re.findall(r"Skills:?\s*(.*)", resume_text)
    if skills_match:
        skills = skills_match[0]

# Output extracted info
print("Extracted Resume Info:")
print("Name:", name)
print("Email:", email)
print("Phone:", phone)
print("Education:", education)
print("Skills:", skills)
