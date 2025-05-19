from DB.connection import get_connection

def ogretmen_guncelle(ogretmen_id, ad, soyad, adres, tel_no, tckn, ogrt_no):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE ogretmenler SET
            ogretmen_adı = ?,
            ogretmen_soyadı = ?,
            ogretmen_adres = ?,
            ogretmen_tel_no = ?,
            ogretmen_tckn = ?,
            ogretmen_numarası = ?
        WHERE ogretmen_id = ?
    """, (ad, soyad, adres, tel_no, tckn, ogrt_no, ogretmen_id))

    conn.commit()
    conn.close()
