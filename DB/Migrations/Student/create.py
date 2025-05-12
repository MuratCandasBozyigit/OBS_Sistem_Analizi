from DB.connection import get_connection

def create_ogrenciler_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ogrenciler (
            ogrenci_id INTEGER PRIMARY KEY AUTOINCREMENT,
            ogrenci_adı TEXT NOT NULL,
            ogrenci_soyadı TEXT NOT NULL,
            ogrenci_fotoğraf TEXT,
            ogrenci_adres TEXT,
            ogrenci_tel_no TEXT,
            ogrenci_tckn TEXT NOT NULL,
            ogrenci_numarası TEXT NOT NULL,
            sifre TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def ogrenci_ekle(ogrenci_adı, ogrenci_soyadı,ogrenci_fotoğraf,ogrenci_adres,ogrenci_tel_no,ogrenci_tcknogrenci_numarası,sifre):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ogrenciler (ders_adı, ders_saati) VALUES (?, ?)",
                   (ders_adi, ders_saati))
    conn.commit()
    conn.close()

