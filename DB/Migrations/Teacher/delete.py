from DB.connection import get_connection

# def ogretmen_sil(ogretmen_id):
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM ogretmenler WHERE ogretmen_id = ?", (ogretmen_id,))
#     conn.commit()
#     conn.close()

def ogretmen_sil(ogretmen_id):
    conn = get_connection()
    cursor = conn.cursor()

    # Önce öğretmenin ders ilişkilerini sil
    cursor.execute("DELETE FROM ogretmen_ders WHERE ogretmen_id = ?", (ogretmen_id,))

    # Sonra öğretmenin kendisini sil
    cursor.execute("DELETE FROM ogretmenler WHERE ogretmen_id = ?", (ogretmen_id,))

    conn.commit()
    conn.close()
