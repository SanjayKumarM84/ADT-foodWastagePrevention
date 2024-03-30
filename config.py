import os

import pyodbc
from dotenv import load_dotenv

load_dotenv()

# Database connection settings
SERVER = os.getenv("SERVER")
DATABASE = os.getenv("DATABASE")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

# Establishing the database connection
def get_db_connection():
    conn_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};TrustServerCertificate=yes'
    conn = pyodbc.connect(conn_str)
    return conn.cursor()
