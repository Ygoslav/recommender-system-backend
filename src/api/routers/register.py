from __future__ import annotations

from fastapi import APIRouter, HTTPException, status

from src import crud
from src.dependencies.db import DatabaseDependency
from src.schemas.users import UserCreateSchema

router = APIRouter()


@router.post('/register', status_code=status.HTTP_201_CREATED)
async def register(db: DatabaseDependency, credentials: UserCreateSchema) -> dict:
    if crud.get_user_by_username(db, credentials.username):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"user with username '{credentials.username}' already exists",
        )
    crud.add_user(db, credentials)
    return {'ok': f"User '{credentials.username}' successfully registered"}
