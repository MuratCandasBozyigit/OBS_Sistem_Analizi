from DB.connection import get_connection

def create_ogretmen_ders_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ogretmen_ders (
            ogretmen_id INTEGER,
            ders_id INTEGER,
            PRIMARY KEY (ogretmen_id, ders_id),
            FOREIGN KEY (ogretmen_id) REFERENCES ogretmenler(ogretmen_id),
            FOREIGN KEY (ders_id) REFERENCES dersler(ders_id)
        )
    ''')
    conn.commit()
    conn.close()
