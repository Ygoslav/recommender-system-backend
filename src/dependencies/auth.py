from typing import Annotated

from fastapi import Depends, HTTPException, status

from src.crud import get_user_by_username
from src.dependencies.credentials import CredentialDependency
from src.dependencies.db import DatabaseDependency
from src.schemas.users import UserBaseSchema, UserCreateSchema


def authorize_user(
    db: DatabaseDependency,
    credentials: CredentialDependency,
) -> None:
    user = get_user_by_username(db, credentials.username)
    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"user with username '{credentials.username}' already exists",
        )
    return UserCreateSchema(username=credentials.username, password=credentials.password)


def authenticate_user(
    db: DatabaseDependency,
    credentials: CredentialDependency,
) -> UserBaseSchema:
    user = get_user_by_username(db, credentials.username)
    if user is None or user.password != credentials.password:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED)
    return user


AuthorizationDependency = Annotated[UserCreateSchema, Depends(authorize_user)]
AuthenticationDependency = Annotated[UserBaseSchema, Depends(authenticate_user)]
