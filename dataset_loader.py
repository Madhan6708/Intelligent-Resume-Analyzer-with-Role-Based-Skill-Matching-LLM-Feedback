from role_skills_dataset import ROLE_SKILLS

def load_role_skills(role):
    role = role.lower().strip()
    return ROLE_SKILLS.get(role, [])
