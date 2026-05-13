from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

try:
    conn = engine.connect()
    print("Connected to FreeSQLDatabase successfully!")
    conn.close()
except Exception as e:
    print("Connection failed:", e)