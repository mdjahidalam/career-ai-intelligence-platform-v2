from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session
from app.core.security import get_current_user

from app.core.database import get_db
from app.repositories.user_repository import UserRepository
from app.schemas.response import APIResponse
from app.services.resume_service import ResumeService
from app.repositories.user_repository import UserRepository
from fastapi import HTTPException
from app.schemas.resume import ResumeResponse

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)


@router.post("/upload", response_model=APIResponse)
def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    resume = ResumeService.upload(
        db,
        current_user,
        file
    )

    return APIResponse(
        success=True,
        message="Resume uploaded successfully",
        data={
            "id": resume.id,
            "filename": resume.original_filename
        }
    )

@router.get("/", response_model=APIResponse)
def list_resumes(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    resumes = ResumeService.get_all(
        db,
        current_user
    )

    return APIResponse(
        success=True,
        message="Resume list fetched successfully",
        data=resumes
    )

@router.post("/analyze/{resume_id}", response_model=APIResponse)
def analyze_resume(

    resume_id: int,

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)

):

    resume = ResumeService.get_by_id(
        db,
        resume_id
    )

    if not resume:
        raise HTTPException(
            status_code=404,
            detail="Resume not found"
        )

    if resume.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    result = ResumeService.analyze(
        db,
        resume
    )

    return APIResponse(

        success=True,

        message="Resume analyzed successfully",

        data=result
    )