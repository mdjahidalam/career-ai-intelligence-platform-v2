from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.auth import UserRegister


class AuthService:

    @staticmethod
    def register(db: Session, user: UserRegister):

        existing_user = UserRepository.get_by_email(db, user.email)

        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="Email already registered"
            )

        new_user = User(
            full_name=user.full_name,
            email=user.email,
            password=hash_password(user.password)
        )

        return UserRepository.create_user(db, new_user)

    @staticmethod
    def login(db: Session, email: str, password: str):

        db_user = UserRepository.get_by_email(db, email)

        if not db_user:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )

        if not verify_password(password, db_user.password):
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )

        token = create_access_token(
            {
                "sub": db_user.email,
                "user_id": db_user.id
            }
        )

        return token