from fastapi import APIRouter
from app.schemas.user import UserCreate, UserResponse

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post(
    "/",
    response_model=UserResponse,
    status_code=201
)
def create_user(user: UserCreate):
    print(f"Recebido novo usario {user.email}")

    mock_db_user = {
        "id": 1, 
        "name": user.name, 
        "email": user.email,
    }

    return UserResponse(**mock_db_user)