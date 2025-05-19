from DB.connection import get_connection

def create_dersler_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dersler (
            ders_id INTEGER PRIMARY KEY AUTOINCREMENT,
            ders_adı TEXT NOT NULL,
            ders_saati INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def ders_ekle(ders_adi, ders_saati):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO dersler (ders_adı, ders_saati) VALUES (?, ?)",
                   (ders_adi, ders_saati))
    conn.commit()
    conn.close()
