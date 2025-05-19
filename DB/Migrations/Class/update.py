from DB.connection import get_connection

def ders_guncelle(ders_id, yeni_ders_adi, yeni_ders_saati):
    # ---------- VALIDASYON ----------
    try:
        yeni_ders_saati = int(yeni_ders_saati)  # Saati int'e çevir
    except ValueError:
        raise ValueError("Ders saati sayısal olmalıdır.")
    
    if not (1 <= yeni_ders_saati <= 30):
        raise ValueError("Ders saati 1 ile 30 arasında olmalıdır.")
    
    # ---------- GÜNCELLEME ----------
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE dersler 
        SET ders_adı = ?, ders_saati = ? 
        WHERE ders_id = ?
    """, (yeni_ders_adi, yeni_ders_saati, ders_id))
    conn.commit()
    conn.close()
