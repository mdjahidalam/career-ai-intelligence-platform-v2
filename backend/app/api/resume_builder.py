"""
==================================================
Resume Builder API
Career AI Intelligence Platform
==================================================
"""

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from fastapi.responses import StreamingResponse

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user

from app.models.user import User

from app.schemas.resume_builder import ResumeRequest

from app.services.resume_builder_service import (
    ResumeBuilderService
)

from app.utils.resume_export.generator import (
    ResumeGenerator
)


router = APIRouter(
    prefix="/resume",
    tags=["Resume Builder"]
)


# ==================================================
# Resume Optimizer
# ==================================================

@router.post("/optimize")
def optimize_resume(

    request: ResumeRequest,

    db: Session = Depends(get_db),

    current_user: User = Depends(get_current_user)

):

    result = ResumeBuilderService.optimize_resume(

        db,

        request.resume_id

    )

    if result is None:

        raise HTTPException(

            status_code=404,

            detail="Resume analysis not found."

        )

    return {

        "success": True,

        "message": "Resume optimized successfully.",

        "data": result

    }


# ==================================================
# Resume Generator
# ==================================================

@router.post("/generate")
def generate_resume(

    request: ResumeRequest,

    db: Session = Depends(get_db),

    current_user: User = Depends(get_current_user)

):

    result = ResumeBuilderService.build_resume(

        db,

        request.resume_id

    )

    if result is None:

        raise HTTPException(

            status_code=404,

            detail="Resume analysis not found."

        )

    return {

        "success": True,

        "message": "Resume generated successfully.",

        "data": result

    }


# ==================================================
# Download Resume DOCX
# ==================================================

@router.post("/download/docx")
def download_resume_docx(

    request: ResumeRequest,

    db: Session = Depends(get_db),

    current_user: User = Depends(get_current_user)

):

    # ------------------------------------------
    # Generate Resume JSON
    # ------------------------------------------

    result = ResumeBuilderService.build_resume(

        db,

        request.resume_id

    )

    if result is None:

        raise HTTPException(

            status_code=404,

            detail="Resume analysis not found."

        )

    # ------------------------------------------
    # Candidate Name
    # ------------------------------------------

    candidate = result.get(

        "candidate",

        {}

    )

    candidate_name = (

        candidate.get(

            "name",

            "Resume"

        )

        .strip()

        .replace(" ", "_")

    )

    # ------------------------------------------
    # Generate DOCX
    # ------------------------------------------

    try:

        file_stream = ResumeGenerator.generate_docx(

            result

        )

    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=f"Unable to generate DOCX resume. {str(e)}"

        )

    # ------------------------------------------
    # Download
    # ------------------------------------------

    return StreamingResponse(

        file_stream,

        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",

        headers={

            "Content-Disposition":

            f'attachment; filename="{candidate_name}_Resume.docx"'

        }

    )