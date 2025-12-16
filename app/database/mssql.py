from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,session
from urllib.parse import quote_plus
import os
import logging

load_dotenv()

class ConfigSettings:

    def __init__(self):
        self.db = os.getenv("DB")
        self.server = os.getenv("SERVER")
        self.user = os.getenv("USER")
        self.pwd = os.getenv("PWD")

    def _connection_string(self):
        conn_str = (
           "Driver={ODBC Driver 17 for SQL Server};"
           f"Server={self.server};"
           f"Database={self.db};"
           f"UID={self.user};"
           f"PWD={self.pwd};"
        )
        encoded_str = quote_plus(conn_str)
        return f"mssql+pyodbc:///?odbc_connect={encoded_str}"

    def engine(self):
        try:
            engine = create_engine(self._connection_string())
            return engine
        except Exception as e:
            logging.critical(f"error occured while connecting sql server engine {str(e)}")
            raise ValueError(f"error occured while connecting sql server engine") from e
        
    def get_db_connection(self)->session:
        try:
            enigne = self.engine()
            sessionMaker = sessionmaker(bind=enigne,autoflush=True,autocommit=False)
            session = sessionMaker()
            return session
        except Exception as e:
            logging.critical(f"error occured while connecting sql server engine {str(e)}")
            raise ValueError(f"error occured while connecting sql server engine") from e


DB = ConfigSettings()
engine= DB.engine()
db = DB.get_db_connection()
    
