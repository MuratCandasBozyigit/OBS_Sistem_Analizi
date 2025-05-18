from DB.connection import get_connection

def ogrenci_ders_ata(ogrenci_id, ders_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR IGNORE INTO ogrenci_ders (ogrenci_id, ders_id)
        VALUES (?, ?)
    ''', (ogrenci_id, ders_id))
    conn.commit()
    conn.close()

def ogrencinin_derslerini_getir(ogrenci_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT d.ders_id, d.ders_adı
        FROM dersler d
        JOIN ogrenci_ders od ON d.ders_id = od.ders_id
        WHERE od.ogrenci_id = ?
    ''', (ogrenci_id,))
    dersler = cursor.fetchall()
    conn.close()
    return dersler

def ogrencinin_ders_sil(ogrenci_id, ders_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM ogrenci_ders
        WHERE ogrenci_id = ? AND ders_id = ?
    ''', (ogrenci_id, ders_id))
    conn.commit()
    conn.close()

def dersi_alan_ogrencileri_getir(ders_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT o.ogrenci_id, o.ogrenci_adı, o.ogrenci_soyadı
        FROM ogrenciler o
        JOIN ogrenci_ders od ON o.ogrenci_id = od.ogrenci_id
        WHERE od.ders_id = ?
    ''', (ders_id,))
    return cursor.fetchall()