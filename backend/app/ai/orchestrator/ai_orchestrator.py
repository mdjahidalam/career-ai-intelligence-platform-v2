from app.ai.agents import AgentFactory
from app.ai.tools.merge_tool import MergeTool


class AIOrchestrator:

    @staticmethod
    def analyze_resume(
        resume_text: str
    ):

        # ----------------------------------------
        # Resume Parsing
        # ----------------------------------------

        resume = AgentFactory.resume().run(
            resume_text
        )

        resume_json = resume.model_dump()

        # ----------------------------------------
        # ATS Analysis
        # ----------------------------------------

        ats = AgentFactory.ats().run(
            resume_json
        )

        # ----------------------------------------
        # Placement Prediction
        # ----------------------------------------

        placement = AgentFactory.placement().run(
            resume_json
        )

        # ----------------------------------------
        # Salary Prediction
        # ----------------------------------------

        salary = AgentFactory.salary().run(
            resume_json
        )

        # ----------------------------------------
        # Career Recommendation
        # ----------------------------------------

        career = AgentFactory.career().run(
            resume_json
        )

        # ----------------------------------------
        # Interview Preparation
        # ----------------------------------------

        interview = AgentFactory.interview().run(
            resume_json
        )

        # ----------------------------------------
        # Resume Optimizer
        # ----------------------------------------

        optimizer = AgentFactory.resume_optimizer().run(
            resume_json
        )

        # ----------------------------------------
        # Resume Builder
        # ----------------------------------------

        # builder = AgentFactory.resume_builder().run(
        #     resume_json
        # )

        # ----------------------------------------
        # Job Matching
        # ----------------------------------------

        # job_matching = AgentFactory.job_matching().run(
        #     resume_json
        # )

        # ----------------------------------------
        # Merge All
        # ----------------------------------------

        final_result = MergeTool.merge(

            resume.model_dump(),

            ats.model_dump(),

            placement.model_dump(),

            salary.model_dump(),

            career.model_dump(),

            interview.model_dump(),

            optimizer.model_dump(),

            # builder.model_dump(),

            # job_matching.model_dump()

        )

        return final_result