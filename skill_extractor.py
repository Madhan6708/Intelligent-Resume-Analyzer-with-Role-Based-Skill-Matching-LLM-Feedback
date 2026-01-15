import re

def normalize(text):
    text = text.lower()
    text = re.sub(r"\s+", "", text)          # remove all spaces
    text = re.sub(r"[^a-z0-9+#.]", "", text) # remove special characters
    return text

def extract_skills_block(resume_text):
    lines = resume_text.split("\n")

    capture = False
    skill_lines = []

    for line in lines:
        line_clean = line.strip().lower()

        # Start when any skill-like header is found
        if any(word in line_clean for word in ["skill", "skills", "technical", "professional", "expertise", "competencies"]):
            capture = True
            continue

        # Stop at next major section
        if capture and any(word in line_clean for word in ["experience", "project", "education", "certification", "internship"]):
            break

        if capture:
            skill_lines.append(line.strip())

    skill_text = " ".join(skill_lines)
    skill_text = normalize(skill_text)

    return skill_text
