required_skills = ['python', 'github', 'linux']

candidates = {
    'anna': {'java', 'linux', 'windows', 'github', 'python', 'full stack'},
    'bob': {'github', 'linux', 'python'},
    'carol': {'linux', 'javascript', 'html', 'python', 'github'},
    'daniel': {'pascal', 'java', 'c++', 'github'},
    'connie': {'html', 'css', 'github', 'python', 'linux'},
    'fenna': {'linux', 'pascal', 'java', 'c', 'lisp', 'modula-2', 'perl', 'github'}
}

# checks for subsets
interviewees = set()
for candidate, skills in candidates.items():
    if skills.issuperset(required_skills):
        interviewees.add(candidate)

print(f"interviewees = {interviewees}")

# To check for proper subset, we need candidates who have more skills than what's required
interviewees_more_skills = set()
required_skills_set = set(required_skills)
for candidate, skills in candidates.items():
    if skills > required_skills_set:
        interviewees_more_skills.add(candidate)

print(f"interviewees_more_skills = {interviewees_more_skills}")