from DB.connection import get_connection

def create_ogrenci_ders_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ogrenci_ders (
            ogrenci_id INTEGER,
            ders_id INTEGER,
            PRIMARY KEY (ogrenci_id, ders_id),
            FOREIGN KEY (ogrenci_id) REFERENCES ogrenciler(ogrenci_id),
            FOREIGN KEY (ders_id) REFERENCES dersler(ders_id)
        )
    ''')
    conn.commit()
    conn.close()
