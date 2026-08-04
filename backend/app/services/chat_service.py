from app.models.chat_session import ChatSession
from app.models.chat_message import ChatMessage

from app.repositories.chat_repository import (
    ChatRepository
)


class ChatService:

    @staticmethod
    def create_session(
        db,
        user,
        title="New Chat"
    ):

        session = ChatSession(

            user_id=user.id,

            title=title

        )

        return ChatRepository.create_session(
            db,
            session
        )

    # ----------------------------------------

    @staticmethod
    def add_message(
        db,
        session,
        role,
        message
    ):

        msg = ChatMessage(

            session_id=session.id,

            role=role,

            message=message

        )

        return ChatRepository.add_message(
            db,
            msg
        )

    # ----------------------------------------

    @staticmethod
    def get_sessions(
        db,
        user
    ):

        return ChatRepository.get_sessions(
            db,
            user.id
        )

    # ----------------------------------------

    @staticmethod
    def get_messages(
        db,
        session_id
    ):

        return ChatRepository.get_messages(
            db,
            session_id
        )