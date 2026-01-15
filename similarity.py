from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_semantic_similarity(resume_text, jd_text):
    embeddings = model.encode([resume_text, jd_text])
    score = cosine_similarity([embeddings[0]], [embeddings[1]])
    return round(float(score[0][0]) * 100, 2)

def compute_skill_match(resume_skills, jd_skills):
    if not jd_skills:
        return 0.0
    matched = set(resume_skills).intersection(set(jd_skills))
    return round((len(matched) / len(jd_skills)) * 100, 2)