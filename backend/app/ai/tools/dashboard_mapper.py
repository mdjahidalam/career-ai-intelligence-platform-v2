class DashboardMapper:

    @staticmethod
    def map(result: dict):

        return {

            "candidate":{

                "name":

                    result.get(
                        "personal_information",
                        {}
                    ).get(
                        "full_name"
                    ),

                "email":

                    result.get(
                        "personal_information",
                        {}
                    ).get(
                        "email"
                    )

            },

            "summary":{

                "ats_score":

                    result.get(
                        "ats",
                        {}
                    ).get(
                        "overall_score"
                    ),

                "placement_probability":

                    result.get(
                        "placement",
                        {}
                    ).get(
                        "placement_probability"
                    ),

                "predicted_salary":

                    result.get(
                        "salary",
                        {}
                    ).get(
                        "predicted_salary"
                    ),

                "career":

                    result.get(
                        "career",
                        {}
                    ).get(
                        "top_recommendation"
                    ),

                "interview_score":

                    result.get(
                        "interview",
                        {}
                    ).get(
                        "overall_score"
                    )

            },

            "skills":

                result.get(
                    "skills",
                    []
                )[:8]

        }