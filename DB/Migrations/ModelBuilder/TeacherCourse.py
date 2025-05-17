    from DB.connection import get_connection

    def ogretmene_ders_ata(ogretmen_id, ders_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR IGNORE INTO ogretmen_ders (ogretmen_id, ders_id)
            VALUES (?, ?)
        ''', (ogretmen_id, ders_id))
        conn.commit()
        conn.close()

    def ogretmenin_derslerini_getir(ogretmen_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT d.ders_id, d.ders_adı
            FROM dersler d
            JOIN ogretmen_ders od ON d.ders_id = od.ders_id
            WHERE od.ogretmen_id = ?
        ''', (ogretmen_id,))
        dersler = cursor.fetchall()
        conn.close()
        return dersler

    def ogretmene_ders_sil(ogretmen_id, ders_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM ogretmen_ders
            WHERE ogretmen_id = ? AND ders_id = ?
        ''', (ogretmen_id, ders_id))
        conn.commit()
        conn.close()


    # def ogretmene_ait_tum_dersleri_sil(ogretmen_id):
    #     conn = get_connection()
    #     cursor = conn.cursor()
    #     cursor.execute('''
    #         DELETE FROM ogretmen_ders
    #         WHERE ogretmen_id = ?
    #     ''', (ogretmen_id,))
    #     conn.commit()
    #     conn.close()
