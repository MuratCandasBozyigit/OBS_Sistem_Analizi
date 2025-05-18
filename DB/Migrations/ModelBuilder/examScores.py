from DB.connection import get_connection

def not_ekle_veya_guncelle(ogrenci_id, ders_id, vize, final):
    ortalama = None
    if vize is not None and final is not None:
        ortalama = (vize * 0.4) + (final * 0.6)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO notlar (ogrenci_id, ders_id, vize, final, ortalama)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(ogrenci_id, ders_id) DO UPDATE SET
            vize=excluded.vize,
            final=excluded.final,
            ortalama=excluded.ortalama
    ''', (ogrenci_id, ders_id, vize, final, ortalama))
    conn.commit()
    conn.close()

def notlari_getir(ogrenci_id, ders_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT vize, final, ortalama
        FROM notlar
        WHERE ogrenci_id = ? AND ders_id = ?
    ''', (ogrenci_id, ders_id))
    result = cursor.fetchone()
    conn.close()
    return result
