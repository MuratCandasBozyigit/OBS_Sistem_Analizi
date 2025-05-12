from DB.connection import get_connection

def ders_guncelle(ders_id, yeni_ders_adi, yeni_ders_saati):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE dersler 
        SET ders_adı = ?, ders_saati = ? 
        WHERE ders_id = ?
    """, (yeni_ders_adi, yeni_ders_saati, ders_id))
    conn.commit()
    conn.close()
