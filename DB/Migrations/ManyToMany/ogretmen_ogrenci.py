from DB.connection import get_connection

def create_ogretmen_ders_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ogretmen_ogrenci (
            ogretmen_id INTEGER,
            ogrenci_id INTEGER,
            PRIMARY KEY (ogretmen_id, ogrenci_id),
            FOREIGN KEY (ogretmen_id) REFERENCES ogretmenler(ogretmen_id),
            FOREIGN KEY (ogrenci_id) REFERENCES ogrenciler(ogrenci_id)
        )
    ''')
    conn.commit()
    conn.close()
