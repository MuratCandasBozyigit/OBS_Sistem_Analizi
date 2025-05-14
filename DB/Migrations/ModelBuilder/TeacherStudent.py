from DB.connection import get_connection

def ogretmene_ogrenci_ata(ogretmen_id, ogrenci_id):
    """
    Verilen öğretmen ve öğrenci ID'lerini eşleştirerek ilişki oluşturur.
    Aynı ilişki varsa tekrar eklemez (INSERT OR IGNORE).
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR IGNORE INTO ogretmen_ogrenci (ogretmen_id, ogrenci_id)
        VALUES (?, ?)
    ''', (ogretmen_id, ogrenci_id))
    conn.commit()
    conn.close()


def ogretmenin_ogrencilerini_getir(ogretmen_id):
    """
    Bir öğretmene atanmış tüm öğrencileri getirir.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT o.ogrenci_id, o.ogrenci_adı, o.ogrenci_soyadı
        FROM ogrenciler o
        INNER JOIN ogretmen_ogrenci oo ON o.ogrenci_id = oo.ogrenci_id
        WHERE oo.ogretmen_id = ?
    ''', (ogretmen_id,))
    ogrenciler = cursor.fetchall()
    conn.close()
    return ogrenciler


def ogrencinin_ogretmenlerini_getir(ogrenci_id):
    """
    Bir öğrenciye atanmış tüm öğretmenleri getirir.
    Bu, öğrenciden öğretmenlere erişim içindir.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT t.ogretmen_id, t.ogretmen_adı, t.ogretmen_soyadı
        FROM ogretmenler t
        INNER JOIN ogretmen_ogrenci oo ON t.ogretmen_id = oo.ogretmen_id
        WHERE oo.ogrenci_id = ?
    ''', (ogrenci_id,))
    ogretmenler = cursor.fetchall()
    conn.close()
    return ogretmenler


def ogretmenden_ogrenci_sil(ogretmen_id, ogrenci_id):
    """
    Belirli bir öğretmen-öğrenci ilişki kaydını siler.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM ogretmen_ogrenci
        WHERE ogretmen_id = ? AND ogrenci_id = ?
    ''', (ogretmen_id, ogrenci_id))
    conn.commit()
    conn.close()
