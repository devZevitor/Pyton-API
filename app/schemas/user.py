from pydantic import BaseModel, Field, EmailStr
from typing import Annotated

class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, description="Nome completo do usuário.")
    email: EmailStr = Field(..., description="Email único do usuário.")
    password: str = Field(..., min_length=8, description="Senha do usuário.")

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True 

