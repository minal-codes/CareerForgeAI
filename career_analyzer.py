def analyze_resume(text):

    text = text.lower()

    score = 40
    ats_score = 40

    strengths = []
    missing = []

    certifications = []
    projects = []
    interview_questions = []
    suggestions = []
    job_roles = []

    # ======================
    # Python
    # ======================

    if "python" in text:
        strengths.append("Python")
        score += 10
        ats_score += 5

        interview_questions.extend([
            "Explain OOP in Python.",
            "Difference between List and Tuple?",
            "What are Python decorators?"
        ])
    else:
        missing.append("Python")
        suggestions.append("Learn Python and add Python projects.")

    # ======================
    # SQL
    # ======================

    if "sql" in text:
        strengths.append("SQL")
        score += 10
        ats_score += 5
    else:
        missing.append("SQL")
        suggestions.append("Learn SQL for data handling.")

    # ======================
    # Azure
    # ======================

    if "azure" in text:
        strengths.append("Azure")
        score += 10
        ats_score += 5

        certifications.append(
            "AI-102 Azure AI Engineer"
        )

        interview_questions.extend([
            "What is Azure Blob Storage?",
            "What is Azure App Service?",
            "Explain Azure Document Intelligence."
        ])

    else:
        missing.append("Azure")
        suggestions.append(
            "Learn Azure Cloud and build Azure projects."
        )

    # ======================
    # Machine Learning
    # ======================

    if "machine learning" in text:
        strengths.append("Machine Learning")
        score += 10
        ats_score += 5

        certifications.append(
            "DP-100 Azure Data Scientist"
        )

        interview_questions.extend([
            "What is Overfitting?",
            "Bias vs Variance?",
            "Supervised vs Unsupervised Learning?"
        ])

    else:
        missing.append("Machine Learning")
        suggestions.append(
            "Add Machine Learning projects."
        )

    # ======================
    # DSA
    # ======================

    if (
        "dsa" in text or
        "data structures" in text or
        "algorithms" in text
    ):
        strengths.append("DSA")
        score += 10
        ats_score += 5
    else:
        missing.append("DSA")
        suggestions.append(
            "Practice DSA for coding interviews."
        )

    # ======================
    # GitHub
    # ======================

    if "github" in text:
        ats_score += 10
    else:
        suggestions.append(
            "Add GitHub profile link."
        )

    # ======================
    # Projects
    # ======================

    if "project" in text:
        ats_score += 10
    else:
        suggestions.append(
            "Add a Projects section."
        )

    # ======================
    # Certifications
    # ======================

    if "certification" in text or "certificate" in text:
        ats_score += 10
    else:
        suggestions.append(
            "Add Certifications section."
        )

    # ======================
    # Job Role Prediction
    # ======================

    if (
        "python" in text and
        "machine learning" in text
    ):
        job_roles.append("AI Engineer")
        job_roles.append("Machine Learning Engineer")

    if (
        "python" in text and
        "sql" in text
    ):
        job_roles.append("Data Scientist")

    if (
        "sql" in text and
        "excel" in text
    ):
        job_roles.append("Data Analyst")

    if "azure" in text:
        job_roles.append("Azure AI Developer")

    if len(job_roles) == 0:
        job_roles = [
            "Software Developer",
            "AI/ML Intern"
        ]

    # ======================
    # Recommended Projects
    # ======================

    projects = [
        "AI Career Mentor",
        "Resume Screening System",
        "Azure RAG Chatbot",
        "AI Interview Coach",
        "Job Recommendation Engine"
    ]

    # ======================
    # Roadmap
    # ======================

    roadmap = [
        "Month 1: Python + SQL",
        "Month 2: DSA + GitHub Portfolio",
        "Month 3: Machine Learning",
        "Month 4: Azure AI Projects",
        "Month 5: Internship Applications"
    ]

    return {
        "score": min(score, 100),
        "ats_score": min(ats_score, 100),
        "strengths": strengths,
        "missing": missing,
        "certifications": certifications,
        "projects": projects,
        "roadmap": roadmap,
        "interview_questions": interview_questions,
        "suggestions": suggestions,
        "job_roles": list(set(job_roles)),
         "summary": """
Candidate possesses skills in Python, Azure and Machine Learning.
Shows potential for AI Engineering roles.
Recommended to strengthen SQL, DSA and build more industry-grade projects.
"""
    }