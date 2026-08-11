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
        print("Resume Agent Started")
        resume = AgentFactory.resume().run(
            resume_text
        )
        print("Resume Agent Done")

        resume_json = resume.model_dump()

        # ----------------------------------------
        # ATS Analysis
        # ----------------------------------------
        print("ATS Agent Started")
        ats = AgentFactory.ats().run(
            resume_json
        )
        print("ATS Agent Done")

        # ----------------------------------------
        # Placement Prediction
        # ----------------------------------------
        print("Placement Agent Started")
        placement = AgentFactory.placement().run(
            resume_json
        )
        print("Placement Agent Done")

        # ----------------------------------------
        # Salary Prediction
        # ----------------------------------------
        print("Salary Agent Started")
        salary = AgentFactory.salary().run(
            resume_json
        )
        print("Salary Agent Done")

        # ----------------------------------------
        # Career Recommendation
        # ----------------------------------------
        print("Career Agent Started")
        career = AgentFactory.career().run(
            resume_json
        )
        print("Career Agent Done")

        # ----------------------------------------
        # Interview Preparation
        # ----------------------------------------
        print("Interview Agent Started")
        interview = AgentFactory.interview().run(
            resume_json
        )
        print("Interview Agent Done")

        # ----------------------------------------
        # Resume Optimizer
        # ----------------------------------------
        print("Resume Optimizer Started")
        optimizer = AgentFactory.resume_optimizer().run(
            resume_json
        )
        print("Resume Optimizer Done")
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

    # ----------------------------------------
    # Resume Optimizer
    # ----------------------------------------

    @staticmethod
    def optimize_resume(
        resume_json: dict
        ):

        print("Resume Optimizer Started")

        optimizer = AgentFactory.resume_optimizer().run(
        resume_json
        )

        print("Resume Optimizer Done")

        return optimizer.model_dump()


    # ----------------------------------------
    # Resume Builder
    # ----------------------------------------

    @staticmethod
    def build_resume(
        resume_json: dict
    ):

        print("Resume Builder Started")

        builder = AgentFactory.resume_builder().run(
            resume_json
        )

        print("Resume Builder Done")

        return builder.model_dump()

