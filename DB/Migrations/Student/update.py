from DB.connection import get_connection
def ogrenci_guncelle(ogrenci_id, ogrenci_adi, ogrenci_soyadi, ogrenci_fotograf, 
                     ogrenci_adres, ogrenci_tel_no, ogrenci_tckn, ogrenci_numarasi, sifre,
                     vize=None, final=None):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE ogrenciler
            SET ogrenci_adı = ?, ogrenci_soyadı = ?, ogrenci_fotoğraf = ?, 
                ogrenci_adres = ?, ogrenci_tel_no = ?, ogrenci_tckn = ?, 
                ogrenci_numarası = ?, sifre = ?, ogrenci_vize = ?, ogrenci_final = ?
            WHERE ogrenci_id = ?
        """, (ogrenci_adi, ogrenci_soyadi, ogrenci_fotograf, ogrenci_adres, 
              ogrenci_tel_no, ogrenci_tckn, ogrenci_numarasi, sifre, vize, final, ogrenci_id))

        conn.commit()
    except Exception as e:
        print("Hata:", e)
    finally:
        conn.close()
