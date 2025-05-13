from DB.connection import get_connection

# def ogrenci_sil(ogrenci_id):
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM ogrenciler WHERE ogrenci_id = ?", (ogrenci_id,))
#     conn.commit()
#     conn.close()


def ogretmen_sil(ogrenci_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM ogretmen_ogrenci WHERE ogrenci_id = ?", (ogrenci_id,))

    cursor.execute("DELETE FROM ogrenciler WHERE ogrenci_id = ?", (ogrenci_id,))

    conn.commit()
    conn.close()
