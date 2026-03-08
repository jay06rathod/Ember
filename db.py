import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

def get_conn():
    return psycopg2.connect(os.environ.get('DATABASE_URL'))

def init_db():
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS URLS (
                id SERIAL PRIMARY KEY,
                short_code TEXT UNIQUE,
                original_url TEXT NOT NULL
            )
        ''')
        conn.commit()
    print("DB initialized ✅")