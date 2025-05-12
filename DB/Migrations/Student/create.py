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


def ogrenci_ekle(ad, soyad, fotoğraf, adres, tel_no, tckn, ogr_no, sifre):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO ogrenciler (
            ogrenci_adı,
            ogrenci_soyadı,
            ogrenci_fotoğraf,
            ogrenci_adres,
            ogrenci_tel_no,
            ogrenci_tckn,
            ogrenci_numarası,
            sifre
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (ad, soyad, fotoğraf, adres, tel_no, tckn, ogr_no, sifre))

    conn.commit()
    conn.close()
