from DB.connection import get_connection

def ogrenci_guncelle(ogrenci_id, ogrenci_adi, ogrenci_soyadi, ogrenci_fotograf, 
                     ogrenci_adres, ogrenci_tel_no, ogrenci_tckn, ogrenci_numarasi, sifre):
    try:
        # Veritabanı bağlantısını al
        conn = get_connection()
        cursor = conn.cursor()

        # Güncelleme sorgusunu çalıştır
        cursor.execute("""
            UPDATE ogrenciler
            SET ogrenci_adi = ?, ogrenci_soyadi = ?, ogrenci_fotoğraf = ?, 
                ogrenci_adres = ?, ogrenci_tel_no = ?, ogrenci_tckn = ?, 
                ogrenci_numarası = ?, sifre = ?
            WHERE ogrenci_id = ?
        """, (ogrenci_adi, ogrenci_soyadi, ogrenci_fotograf, ogrenci_adres, 
              ogrenci_tel_no, ogrenci_tckn, ogrenci_numarasi, sifre, ogrenci_id))

        conn.commit()

    except Exception :
        pass
    finally:
        conn.close()
