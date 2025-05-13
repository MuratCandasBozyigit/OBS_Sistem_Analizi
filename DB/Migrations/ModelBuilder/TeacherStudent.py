from DB.connection import get_connection

def ogretmene_ogrenci_ata(ogretmen_id, ogrenci_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR IGNORE INTO ogretmen_ogrenci (ogretmen_id, ogrenci_id)
        VALUES (?, ?)
    ''', (ogretmen_id, ogrenci_id))
    conn.commit()
    conn.close()

def ogretmenin_ogrencilerini_getir(ogretmen_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT d.ogrenci_id, d.ogrenci_adı,d.ogrenci_soyadı
        FROM ogrenciler d
        JOIN ogretmen_ogrenci od ON d.ogrenci_id = od.ders_id
        WHERE od.ogretmen_id = ?
    ''', (ogretmen_id,))
    dersler = cursor.fetchall()
    conn.close()
    return dersler

def ogretmene_ogrencilerini_sil(ogretmen_id, ogrenci_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM ogretmen_ogrenci
        WHERE ogretmen_id = ? AND ogrenci_id = ?
    ''', (ogretmen_id, ogrenci_id))
    conn.commit()
    conn.close()


