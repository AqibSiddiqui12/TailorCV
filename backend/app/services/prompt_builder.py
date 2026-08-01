# prompt_builder.py
# Purpose: assemble the system + user prompt sent to Claude (Phase 4).

# def get_cv_type_conventions(cv_type: CVType) -> str:
#     - Returns the style ruleset text block:
#       TECH -> skills-forward, concise action bullets, quantified impact, tech-stack emphasis
#       BUSINESS -> achievement/outcome-based narrative bullets

# def build_system_prompt(cv_type: CVType, language: Language) -> str:
#     - Combines get_cv_type_conventions(cv_type) with a language instruction line
#       ("Write all output in German/English") — language only affects output language,
#       never structure/conventions
#     - Includes the hard constraint: never invent experience/skills not present in source

# def trim_input_text(text: str) -> str:
#     - Strips redundant whitespace/line breaks before sending to Claude
#     - Keeps prompt lean for cost control

# def build_user_prompt(master_resume: str, job_description: str) -> str:
#     - Trims both inputs via trim_input_text()
#     - Assembles the task instruction: "Here is the master resume (facts only) and
#       the job description — decide section order, emphasis, and rewrite bullets
#       accordingly"
