import ollama

def get_llm_feedback(role, matched_skills, missing_skills):
    prompt = f"""
You are a senior hiring manager reviewing a resume for the role: {role}.

The candidate has the following matched skills:
{", ".join(matched_skills)}

The candidate is missing the following important skills:
{", ".join(missing_skills)}

TASK:
1. Give a clear verdict: Strong fit / Moderate fit / Weak fit – and explain why.
2. List exactly 3 specific improvement suggestions.
3. Rewrite ONE resume bullet to better align with the {role} role.

IMPORTANT RULES:
- Be concise and professional.
- Do not mention that you are an AI.
- Do not repeat the skill lists.
- Make feedback sound like real recruiter feedback.
- No generic advice.

Output format:

Fit:
<your answer>

Improvements:
- ...
- ...
- ...

Rewritten Bullet:
<your rewritten bullet>
"""

    response = ollama.chat(
    model="phi3",
    messages=[{"role": "user", "content": prompt}]
)


    return response["message"]["content"]
