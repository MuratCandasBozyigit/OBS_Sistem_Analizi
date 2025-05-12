from DB.connection import get_connection

def ders_sil(ders_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM dersler WHERE ders_id = ?", (ders_id,))
    conn.commit()
    conn.close()
