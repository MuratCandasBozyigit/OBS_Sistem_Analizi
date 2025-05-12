from DB.connection import get_connection

def tum_ogrencileri_getir():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ogrenciler")
    student = cursor.fetchall()
    conn.close()
    return student
