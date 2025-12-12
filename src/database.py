import os
from collections.abc import Generator

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

load_dotenv()


class Base(DeclarativeBase):
    pass


DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)

new_session_factory = sessionmaker(engine, expire_on_commit=False)


def get_session() -> Generator[Session, None, None]:
    with new_session_factory() as session:
        yield session
