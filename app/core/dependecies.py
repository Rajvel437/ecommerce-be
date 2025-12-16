# from app.database.mssql import get_db_connection

from fastapi import Depends
from sqlalchemy.orm import Session
from app.database.mssql import DB


def get_db()->Session:
    db = DB.get_db_connection()
    try:
        yield db
    finally:
        db.close()







