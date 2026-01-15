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

ai-resume-analyzer/
├── app.py
├── resume_parser.py
├── skill_extractor.py
├── dataset_loader.py
├── role_skills_dataset.py
├── llm_feedback.py
├── requirements.txt
└── README.md

yaml
Copy code

---

## ⚙️ Installation & Setup

1. Clone the repository:
git clone https://github.com/your-username/ai-resume-analyzer.git
cd ai-resume-analyzer

2.Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3.Install dependencies:
pip install -r requirements.txt

4.Install Ollama and pull model:
ollama pull phi3

5.Run the application:
streamlit run app.py
