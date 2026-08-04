from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user

from app.services.chat_service import ChatService

router = APIRouter(

    prefix="/chat",

    tags=["Chat"]

)


@router.get("/sessions")

def get_sessions(

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)

):

    return ChatService.get_sessions(

        db,

        current_user

    )