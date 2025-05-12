from DB.connection import get_connection

def tum_dersleri_getir():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dersler")
    dersler = cursor.fetchall()
    conn.close()
    return dersler
