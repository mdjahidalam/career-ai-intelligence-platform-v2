from app.ai.orchestrator import AIOrchestrator

resume_text = """

Your Resume Text Here

"""

result = AIOrchestrator.analyze_resume(
    resume_text
)

print(result)