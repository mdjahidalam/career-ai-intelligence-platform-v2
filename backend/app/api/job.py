from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user

from app.services.job_matching_service import (
    JobMatchingService
)

router = APIRouter(

    prefix="/job",

    tags=["Job Matching"]

)


@router.get("/{resume_id}")

def get_matches(

    resume_id: int,

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)

):

    return JobMatchingService.get_resume_matches(

        db,

        resume_id

    )