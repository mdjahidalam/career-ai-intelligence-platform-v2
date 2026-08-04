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
from fastapi.responses import JSONResponse
from app.services.resume_ai_analysis_service import ResumeAIAnalysisService

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

@router.get(
    "/{resume_id}",
    response_model=APIResponse
)
def get_resume(

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

    return APIResponse(

        success=True,

        message="Resume fetched successfully",

        data=ResumeResponse.model_validate(
            resume
        )

    )

@router.get(
    "/analysis/{resume_id}",
    response_model=APIResponse
)
def get_analysis(

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

    analysis = ResumeAIAnalysisService.get_by_resume(

        db,

        resume.id

    )

    if not analysis:

        raise HTTPException(

            status_code=404,

            detail="Analysis not found"

        )

    return APIResponse(

        success=True,

        message="Analysis fetched successfully",

        data=analysis.parsed_json

    )

@router.get(
    "/dashboard/{resume_id}",
    response_model=APIResponse
)
def dashboard(

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

    dashboard = ResumeAIAnalysisService.dashboard(

        db,

        resume.id

    )

    if dashboard is None:

        raise HTTPException(

            status_code=404,

            detail="Analysis not found"

        )

    return APIResponse(

        success=True,

        message="Dashboard fetched successfully",

        data=dashboard

    )

@router.delete(
    "/{resume_id}",
    response_model=APIResponse
)
def delete_resume(

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

    ResumeService.delete(
        db,
        resume
    )

    return APIResponse(

        success=True,

        message="Resume deleted successfully",

        data=None

    )

@router.get(
    "/download-analysis/{resume_id}"
)
def download_analysis(

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

    analysis = ResumeAIAnalysisService.get_by_resume(
        db,
        resume.id
    )

    if not analysis:

        raise HTTPException(
            status_code=404,
            detail="Analysis not found"
        )

    return JSONResponse(

        content=analysis.parsed_json,

        headers={
            "Content-Disposition":
            f'attachment; filename="resume_analysis_{resume.id}.json"'
        }

    )