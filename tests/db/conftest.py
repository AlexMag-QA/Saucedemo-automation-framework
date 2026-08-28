import os

import psycopg
import pytest
from dotenv import load_dotenv
from psycopg.rows import dict_row
from database.users_repository import UsersRepository

load_dotenv()


@pytest.fixture
def db_cursor():
    connection = psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        row_factory=dict_row
    )

    cursor = connection.cursor()

    try:
        yield cursor
    finally:
        connection.rollback()
        cursor.close()
        connection.close()


@pytest.fixture
def users_repository(db_cursor):
    return UsersRepository(db_cursor)
