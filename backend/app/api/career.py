from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user

from app.services.career_service import CareerService
from typing import List

from app.schemas.career import CareerResponse


router = APIRouter(
    prefix="/career",
    tags=["Career"]
)


@router.get(

    "/{resume_id}",

    response_model=List[CareerResponse]

)
def get_career_recommendations(

    resume_id: int,

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)

):

    return CareerService.get_by_resume(

        db,

        resume_id

    )