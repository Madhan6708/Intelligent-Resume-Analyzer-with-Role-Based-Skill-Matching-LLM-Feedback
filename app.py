import streamlit as st
from llm_feedback import get_llm_feedback
from resume_parser import extract_resume_text
from skill_extractor import extract_skills_block
from dataset_loader import load_role_skills
import re

st.title("Intelligent Resume Analyzer with Role-Based Skill Matching & LLM Feedback")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
role = st.text_input("Enter Job Role (e.g. Data Scientist, Data Analyst)")

def normalize_skill(skill):
    skill = skill.lower()
    skill = re.sub(r"\s+", "", skill)
    skill = re.sub(r"[^a-z0-9+#.]", "", skill)
    return skill

if st.button("Analyze"):
    if not resume_file:
        st.error("Please upload a resume.")
        st.stop()

    if not role:
        st.error("Please enter a role.")
        st.stop()

    # ✅ THIS WAS MISSING
    resume_text = extract_resume_text(resume_file)

    # ✅ NOW this will work
    skills_block_text = extract_skills_block(resume_text)

    # Load dataset skills
    role_skills = load_role_skills(role)

    matched_skills = []
    missing_skills = []

    for skill in role_skills:
        skill_norm = normalize_skill(skill)

        if skill_norm in skills_block_text:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    match_percentage = round((len(matched_skills) / len(role_skills)) * 100, 2) if role_skills else 0.0

    st.subheader("Results")
    st.write(f"Match Percentage: {match_percentage}%")
    st.write("Matched Skills:", matched_skills)
    st.write("Missing Skills:", missing_skills)
    st.subheader("LLM Feedback")

    llm_feedback = get_llm_feedback(role, matched_skills, missing_skills)

    # Render nicely formatted markdown
    st.markdown(llm_feedback)

