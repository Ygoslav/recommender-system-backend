from typing import Annotated

from fastapi import Depends, HTTPException, status

from src.crud import get_user_by_username
from src.dependencies.credentials import CredentialDependency
from src.dependencies.db import DatabaseDependency
from src.schemas.users import UserBaseSchema


def authenticate_user(
    db: DatabaseDependency,
    credentials: CredentialDependency,
) -> UserBaseSchema:
    user = get_user_by_username(db, credentials.username)
    if user is None or user.password != credentials.password:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED)
    return user


AuthenticationDependency = Annotated[UserBaseSchema, Depends(authenticate_user)]
