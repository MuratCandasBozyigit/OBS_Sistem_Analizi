from DB.connection import get_connection

def create_ogretmenler_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ogretmenler (
            ogretmen_id INTEGER PRIMARY KEY AUTOINCREMENT,
            ogretmen_adı TEXT NOT NULL,
            ogretmen_soyadı TEXT NOT NULL,
            ogretmen_fotoğraf TEXT,
            ogretmen_adres TEXT,
            ogretmen_tel_no TEXT,
            ogretmen_tckn TEXT NOT NULL,
            ogretmen_numarası TEXT NOT NULL,
            şifre TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
