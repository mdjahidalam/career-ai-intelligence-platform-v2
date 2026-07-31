class FeatureEngineeringService:

    @staticmethod
    def extract_features(resume_json):

        features = {}

        features["cgpa"] = 0

        features["projects"] = len(
            resume_json.projects
        )

        features["certifications"] = len(
            resume_json.certifications
        )

        features["languages"] = len(
            resume_json.languages
        )

        features["education"] = len(
            resume_json.education
        )

        return features