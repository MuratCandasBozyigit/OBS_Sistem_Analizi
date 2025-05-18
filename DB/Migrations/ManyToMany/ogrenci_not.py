from DB.connection import get_connection

def create_notlar_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notlar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ogrenci_id INTEGER NOT NULL,
            ders_id INTEGER NOT NULL,
            vize REAL,
            final REAL,
            ortalama REAL,
            UNIQUE (ogrenci_id, ders_id),
            FOREIGN KEY (ogrenci_id) REFERENCES ogrenciler(ogrenci_id),
            FOREIGN KEY (ders_id) REFERENCES dersler(ders_id)
        )
    ''')
    conn.commit()
    conn.close()
