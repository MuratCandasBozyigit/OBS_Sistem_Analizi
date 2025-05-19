from DB.connection import get_connection

def create_ogretmenler_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ogretmenler (
            ogretmen_id INTEGER PRIMARY KEY AUTOINCREMENT,
            ogretmen_adı TEXT NOT NULL,
            ogretmen_soyadı TEXT NOT NULL,
            ogretmen_adres TEXT,
            ogretmen_tel_no TEXT,
            ogretmen_tckn TEXT NOT NULL,
            ogretmen_numarası INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def ogretmen_ekle(ad, soyad, adres, tel_no, tckn, ogrt_no):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO ogretmenler (
            ogretmen_adı,
            ogretmen_soyadı,
            ogretmen_adres,
            ogretmen_tel_no,
            ogretmen_tckn,
            ogretmen_numarası
        ) VALUES (?, ?, ?, ?, ?, ?)
    """, (ad, soyad, adres, tel_no, tckn, ogrt_no))

    conn.commit()
    conn.close()
