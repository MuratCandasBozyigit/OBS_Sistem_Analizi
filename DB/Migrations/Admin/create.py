from DB.connection import get_connection

def create_adminler_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS adminler (
            admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
            ad TEXT NOT NULL,
            soyad TEXT NOT NULL,
            kullanici_adi TEXT NOT NULL UNIQUE,
            sifre TEXT NOT NULL
        );
    ''')

    conn.commit()
    
