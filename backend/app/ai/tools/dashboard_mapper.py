class DashboardMapper:

    @staticmethod
    def map(result: dict):

        skills = result.get("skills", {})

        all_skills = []

        if isinstance(skills, dict):

            for value in skills.values():

                if isinstance(value, list):

                    all_skills.extend(value)

        elif isinstance(skills, list):

            all_skills = skills

        # ==========================================
        # Merge Recommendations
        # ==========================================

        recommendations = []

        recommendations.extend(

            result.get(

                "improvement_suggestions",

                []

            )

        )

        recommendations.extend(

            result.get(

                "ats_friendly_recommendations",

                []

            )

        )

        return {

            "candidate": {

                "name": result.get(

                    "personal_information",

                    {}

                ).get("name"),

                "email": result.get(

                    "personal_information",

                    {}

                ).get("email")

            },

            "summary": {

                "ats_score": result.get(

                    "ats_score"

                ),

                "placement_probability": result.get(

                    "placement_probability"

                ),

                "predicted_salary": result.get(

                    "india_salary_range"

                ),

                "career": result.get(

                    "career_profile",

                    {}

                ).get("primary_role"),

                "interview_score": result.get(

                    "overall_readiness"

                )

            },

            # All Skills

            "skills": all_skills,

            # ATS

            "strengths": result.get(

                "strengths",

                []

            ),

            "weaknesses": result.get(

                "weaknesses",

                []

            ),

            # Recommendations

            "recommendations": recommendations,

            "status": "completed"

        }