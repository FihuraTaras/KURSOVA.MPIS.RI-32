from database import create_connection
from datetime import datetime

def add_log(action, user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO logs (action, timestamp, user_id) VALUES (?, ?, ?)', (action, datetime.now(), user_id))
    conn.commit()
    conn.close()
