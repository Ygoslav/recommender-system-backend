from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()
CredentialDependency = Annotated[HTTPBasicCredentials, Depends(security)]
