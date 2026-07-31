import os
import uuid

from app.models.resume import Resume
from app.repositories.resume_repository import ResumeRepository

from app.schemas.resume import ResumeResponse

from app.ai.resume_parser import ResumeParser
from app.ai.llm_extractor import LLMExtractor
from fastapi import HTTPException
from app.services.resume_ai_analysis_service import (
            ResumeAIAnalysisService
        )

class ResumeService:

    UPLOAD_DIR = "uploads/resumes"

    @staticmethod
    def upload(db, user, file):

        extension = file.filename.split(".")[-1]

        filename = f"{uuid.uuid4()}.{extension}"

        os.makedirs(ResumeService.UPLOAD_DIR, exist_ok=True)

        filepath = os.path.join(
            ResumeService.UPLOAD_DIR,
            filename
        )

        with open(filepath, "wb") as buffer:
            buffer.write(file.file.read())

        resume = Resume(
            user_id=user.id,
            original_filename=file.filename,
            stored_filename=filename,
            file_path=filepath,
            file_size=os.path.getsize(filepath),
            file_type=extension
        )

        resume = ResumeRepository.create(db, resume)
        return resume

    @staticmethod
    def get_all(db, user):

        resumes = ResumeRepository.get_all_by_user(
            db,
            user.id)

        return [
            ResumeResponse.model_validate(resume)
            for resume in resumes
        ]

    @staticmethod
    def get_by_id(db, resume_id):
        return ResumeRepository.get_by_id(
            db,
            resume_id
        )

    @staticmethod
    def delete(db, resume):
        import os

        if os.path.exists(resume.file_path):
            os.remove(resume.file_path)

        ResumeRepository.delete(db, resume)

    @staticmethod
    def analyze(db, resume):

        text = ResumeParser.extract_text(
            resume.file_path)

        analysis = LLMExtractor.extract_resume(text)
        
        ResumeAIAnalysisService.save_analysis(
            db,
            resume,
            analysis
        )
        return analysis
        