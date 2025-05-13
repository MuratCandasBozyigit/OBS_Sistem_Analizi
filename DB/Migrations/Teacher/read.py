from DB.connection import get_connection

def tum_ogretmenleri_getir():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ogretmenler")
    student = cursor.fetchall()
    conn.close()
    return student
