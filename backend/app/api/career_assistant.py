from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user

from app.models.user import User

from app.ai.schemas.career_assistant_schema import (
    CareerChatRequest
)

from app.services.career_assistant_service import (
    CareerAssistantService
)
from fastapi.responses import StreamingResponse
from app.models.chat_session import ChatSession
from app.models.chat_message import ChatMessage

router = APIRouter(
    prefix="/career",
    tags=["Career AI Assistant"]
)


# ==========================================
# Career AI Chat
# ==========================================

@router.post("/chat")
def career_chat(

    request: CareerChatRequest,

    db: Session = Depends(
        get_db
    ),

    current_user: User = Depends(
        get_current_user
    )

):

    # ==========================================
    # Validate Message
    # ==========================================

    message = request.message.strip()

    if not message:

        raise HTTPException(

            status_code=400,

            detail="Message cannot be empty."

        )


    # ==========================================
    # Generate AI Response
    # ==========================================

    try:

        result = CareerAssistantService.chat(

            db=db,

            user=current_user,

            message=message,

            conversation_id=
                request.conversation_id

        )

    except Exception as exc:

        print(
            "Career AI Error:",
            exc
        )

        raise HTTPException(

            status_code=500,

            detail="Unable to generate AI response."

        )


    # ==========================================
    # Response
    # ==========================================

    return {

        "success": True,

        "data": result

    }


# ==========================================
# Get Chat History
# ==========================================

@router.get("/history")
def get_chat_history(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    sessions = (
        db.query(ChatSession)
        .filter(
            ChatSession.user_id == current_user.id
        )
        .order_by(
            ChatSession.updated_at.desc()
        )
        .all()
    )

    return {
        "success": True,
        "data": [
            {
                "id": session.id,
                "title": session.title,
                "created_at": session.created_at,
                "updated_at": session.updated_at
            }
            for session in sessions
        ]
    }


# ==========================================
# Get Single Conversation
# ==========================================

@router.get("/history/{conversation_id}")
def get_conversation(
    conversation_id: int,

    db: Session = Depends(get_db),

    current_user: User = Depends(
        get_current_user
    )
):

    session = (
        db.query(ChatSession)
        .filter(
            ChatSession.id == conversation_id,

            ChatSession.user_id ==
            current_user.id
        )
        .first()
    )

    if session is None:

        raise HTTPException(
            status_code=404,
            detail="Conversation not found."
        )

    messages = (
        db.query(ChatMessage)
        .filter(
            ChatMessage.session_id ==
            session.id
        )
        .order_by(
            ChatMessage.created_at.asc()
        )
        .all()
    )

    return {

        "success": True,

        "data": {

            "id": session.id,

            "title": session.title,

            "messages": [

                {
                    "id": message.id,

                    "role": message.role,

                    "message": message.message,

                    "created_at":
                        message.created_at

                }

                for message in messages

            ]

        }

    }


# ==========================================
# Delete Conversation
# ==========================================

@router.delete("/history/{conversation_id}")
def delete_conversation(
    conversation_id: int,

    db: Session = Depends(get_db),

    current_user: User = Depends(
        get_current_user
    )
):

    session = (
        db.query(ChatSession)
        .filter(
            ChatSession.id == conversation_id,

            ChatSession.user_id ==
            current_user.id
        )
        .first()
    )

    if session is None:

        raise HTTPException(
            status_code=404,
            detail="Conversation not found."
        )

    db.delete(session)

    db.commit()

    return {

        "success": True,

        "message":
            "Conversation deleted successfully."

    }

# ==========================================
# Rename Conversation
# ==========================================

@router.put("/history/{conversation_id}/rename")
def rename_conversation(

    conversation_id: int,

    request: dict,

    db: Session = Depends(get_db),

    current_user: User = Depends(
        get_current_user
    )

):

    # ==========================================
    # Get New Title
    # ==========================================

    title = request.get(
        "title",
        ""
    ).strip()


    if not title:

        raise HTTPException(

            status_code=400,

            detail="Title cannot be empty."

        )


    if len(title) > 100:

        raise HTTPException(

            status_code=400,

            detail="Title cannot exceed 100 characters."

        )


    # ==========================================
    # Find Conversation
    # ==========================================

    session = (

        db.query(ChatSession)

        .filter(

            ChatSession.id ==
                conversation_id,

            ChatSession.user_id ==
                current_user.id

        )

        .first()

    )


    if session is None:

        raise HTTPException(

            status_code=404,

            detail="Conversation not found."

        )


    # ==========================================
    # Update Title
    # ==========================================

    session.title = title


    db.commit()

    db.refresh(session)


    # ==========================================
    # Response
    # ==========================================

    return {

        "success": True,

        "data": {

            "id": session.id,

            "title": session.title

        }

    }

# ==========================================
# Career AI Streaming Chat
# ==========================================

@router.post("/chat/stream")
def career_chat_stream(

    request: CareerChatRequest,

    db: Session = Depends(
        get_db
    ),

    current_user: User = Depends(
        get_current_user
    )

):

    # ==========================================
    # Validate Message
    # ==========================================

    message = request.message.strip()

    if not message:

        raise HTTPException(

            status_code=400,

            detail="Message cannot be empty."

        )


    # ==========================================
    # Create Stream
    # ==========================================

    try:

        stream = CareerAssistantService.stream_chat(

            db=db,

            user=current_user,

            message=message,

            conversation_id=
                request.conversation_id

        )


        # ==========================================
        # Return SSE Response
        # ==========================================

        return StreamingResponse(

            stream,

            media_type="text/event-stream",

            headers={

                "Cache-Control":
                    "no-cache",

                "Connection":
                    "keep-alive",

                "X-Accel-Buffering":
                    "no"

            }

        )


    except Exception as exc:

        print(
            "Career AI Streaming Error:",
            exc
        )

        raise HTTPException(

            status_code=500,

            detail="Unable to generate AI response."

        )