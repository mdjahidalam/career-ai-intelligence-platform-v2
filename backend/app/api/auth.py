from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core.security import get_current_user
from app.core.database import get_db
from app.core.security import verify_access_token
from app.schemas.auth import UserRegister
from app.services.auth_service import AuthService
from app.schemas.response import APIResponse

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.get("/")
def auth_home():
    return {
        "message": "Authentication Service"
    }


@router.post("/register", response_model=APIResponse)
def register_user(
    user: UserRegister,
    db: Session = Depends(get_db)
):
    new_user = AuthService.register(db, user)

    return APIResponse(
        success=True,
        message="User registered successfully",
        data={
            "id": new_user.id,
            "full_name": new_user.full_name,
            "email": new_user.email
        }
    )


@router.post("/login")
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    token = AuthService.login(
        db,
        form_data.username,
        form_data.password
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@router.get("/me", response_model=APIResponse)
def me(
    current_user = Depends(get_current_user)
):
    return APIResponse(
        success=True,
        message="User fetched successfully",
        data={
            "id": current_user.id,
            "full_name": current_user.full_name,
            "email": current_user.email
        }
    )