import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')  # Connect to the SQLite database
    conn.row_factory = sqlite3.Row  # Enable row access by name
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    # Create a sample table (you can modify this as needed)
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        email TEXT NOT NULL)''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()  # Initialize the database when this file is run
