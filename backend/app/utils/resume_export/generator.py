"""
==================================================
Resume Export Generator
==================================================
"""

from io import BytesIO

from .templates import MicrosoftResumeTemplate


class ResumeGenerator:

    """
    Resume Export Engine

    Supported Formats

    - Microsoft DOCX
    - PDF (Future)
    - HTML (Future)
    """

    @staticmethod
    def generate_docx(

        resume_data: dict

    ) -> BytesIO:

        document = MicrosoftResumeTemplate.build(

            resume_data

        )

        output = BytesIO()

        document.save(output)

        output.seek(0)

        return output