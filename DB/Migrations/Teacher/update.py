from DB.connection import get_connection


def ogretmen_guncelle(ogretmen_id, ad, soyad, fotoğraf, adres, tel_no, tckn, ogrt_no, sifre):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE ogretmenler SET
            ogretmen_adı = ?,
            ogretmen_soyadı = ?,
            ogretmen_fotoğraf = ?,
            ogretmen_adres = ?,
            ogretmen_tel_no = ?,
            ogretmen_tckn = ?,
            ogretmen_numarası = ?,
            şifre = ?
        WHERE ogretmen_id = ?
    """, (ad, soyad, fotoğraf, adres, tel_no, tckn, ogrt_no, sifre, ogretmen_id))

    conn.commit()
    conn.close()
