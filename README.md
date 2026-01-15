# Intelligent Resume Analyzer with Role-Based Skill Matching & LLM Feedback

An AI-powered resume analysis system that extracts skills from resumes, matches them against predefined role requirements, calculates a match score, identifies missing skills, and generates recruiter-style feedback using a local LLM.

This project simulates how modern ATS (Applicant Tracking Systems) screen candidates by combining deterministic logic with AI-driven insights.

---

## 🚀 Features

- Extracts skills directly from resume PDFs (format independent)
- Normalizes and matches skills against role-specific datasets
- Calculates skill match percentage
- Highlights matched and missing skills
- Generates recruiter-style feedback using local LLM (Ollama)
- Rewrites resume bullets aligned to the target role
- Fully offline and deterministic matching logic

---

## 🛠 Tech Stack

- Python
- Streamlit
- Regex & Text Normalization
- PDF Parsing (pdfplumber, pytesseract)
- Ollama (Local LLM Inference)
- Phi-3 / TinyLlama models

---

## 📂 Project Structure

