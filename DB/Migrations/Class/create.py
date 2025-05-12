from DB.connection import get_connection

def create_dersler_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dersler (
            ders_id INTEGER PRIMARY KEY AUTOINCREMENT,
            ders_adı TEXT NOT NULL,
            ders_saati TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
