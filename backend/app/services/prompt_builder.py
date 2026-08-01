from app.models.enums import CVType, Language


def get_cv_type_conventions(cv_type: CVType) -> str:
    if cv_type == CVType.TECH:
        return (
            "Use a skills-first resume. "
            "Use concise action-oriented bullet points. "
            "Highlight the tech stack. "
            "Quantify achievements wherever possible."
        )

    return (
        "Use achievement-focused bullet points. "
        "Emphasize business impact and measurable outcomes. "
        "Maintain a professional narrative style."
    )


def build_system_prompt(cv_type: CVType, language: Language) -> str:
    conventions = get_cv_type_conventions(cv_type)

    if language == Language.ENGLISH:
        language_instruction = "Write all output in English."
    else:
        language_instruction = "Write all output in German."

    hard_constraints = (
        "Never invent experience, skills, projects, education, certifications, "
        "or achievements. Only reorder, emphasize, and rewrite information that "
        "already exists in the master resume. Return a complete, well-structured resume."
    )

    return (
        f"You are an expert resume editor.\n\n"
        f"{language_instruction}\n\n"
        f"Resume conventions:\n"
        f"{conventions}\n\n"
        f"Rules:\n"
        f"{hard_constraints}"
    )


def trim_input_text(text: str) -> str:
    lines = text.splitlines()
    trimmed_lines = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        trimmed_lines.append(line)

    return "\n".join(trimmed_lines)


def build_user_prompt(master_resume: str, job_description: str) -> str:
    master_resume = trim_input_text(master_resume)
    job_description = trim_input_text(job_description)

    return f"""
Here is the master resume. Treat it as the source of truth. Do not invent any facts.

Master Resume:
{master_resume}

Job Description:
{job_description}

Your task:
- Read both documents carefully.
- Decide the best section order.
- Decide what to emphasize first.
- Rewrite the bullet points to match the job description.
- Never invent experience, skills, education, projects, or achievements.
""".strip()