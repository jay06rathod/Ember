import sqlite3

def init_db():
    with sqlite3.connect('urls.db') as conn:
        cursor = conn.cursor() # cursor is a medium through which we operate SQL commands and receive the signals
        # No need for conn.close() as with the context manager(with) it is automatically closed, thanks to python
        print("DB is created and connected successfully! ✅")

        create_table_query = '''
        CREATE TABLE IF NOT EXISTS URLS(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            short_code TEXT UNIQUE,
            original_url TEXT NOT NULL
        );
        '''
        
        cursor.execute(create_table_query)
        conn.commit()

        print("Table 'URLS' created successfully! ✅")

init_db()