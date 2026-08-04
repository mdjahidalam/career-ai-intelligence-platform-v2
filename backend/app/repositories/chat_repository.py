from sqlalchemy.orm import Session

from app.models.chat_session import ChatSession
from app.models.chat_message import ChatMessage


class ChatRepository:

    @staticmethod
    def create_session(
        db: Session,
        session: ChatSession
    ):

        db.add(session)
        db.commit()
        db.refresh(session)

        return session

    @staticmethod
    def get_sessions(
        db: Session,
        user_id: int
    ):

        return (
            db.query(ChatSession)
            .filter(
                ChatSession.user_id == user_id
            )
            .all()
        )

    @staticmethod
    def add_message(
        db: Session,
        message: ChatMessage
    ):

        db.add(message)
        db.commit()
        db.refresh(message)

        return message

    @staticmethod
    def get_messages(
        db: Session,
        session_id: int
    ):

        return (
            db.query(ChatMessage)
            .filter(
                ChatMessage.session_id == session_id
            )
            .all()
        )