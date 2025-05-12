import sqlite3
import os

DB_PATH = os.path.join(os.getcwd(), "okul.db")

def get_connection():
    return sqlite3.connect(DB_PATH)


#def init_database()
#     # Bağlantıyı al
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()

#     # Dersler Tablosunu Oluştur
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS dersler (
#         ders_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         ders_adı TEXT NOT NULL,
#         ders_saati TEXT NOT NULL
#     );
#     ''')

#     # Öğrenciler Tablosunu Oluştur
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS ogrenciler (
#         ogrenci_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         ogrenci_adı TEXT NOT NULL,
#         ogrenci_soyadı TEXT NOT NULL,
#         ogrenci_fotoğraf TEXT,
#         ogrenci_adres TEXT,
#         ogrenci_tel_no TEXT,
#         ogrenci_tckn TEXT NOT NULL,
#         ogrenci_numarası TEXT NOT NULL,
#         şifre TEXT NOT NULL
#     );
#     ''')

#     # Öğretmenler Tablosunu Oluştur
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS ogretmenler (
#         ogretmen_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         ogretmen_adı TEXT NOT NULL,
#         ogretmen_soyadı TEXT NOT NULL,
#         ogretmen_fotoğraf TEXT,
#         ogretmen_adres TEXT,
#         ogretmen_tel_no TEXT,
#         ogretmen_tckn TEXT NOT NULL,
#         ogretmen_numarası TEXT NOT NULL,
#         şifre TEXT NOT NULL
#     );
#     ''')

#     # Değişiklikleri kaydet ve bağlantıyı kapat
#     conn.commit()
#     conn.close()

# # Tabloyu oluşturma fonksiyonunu çalıştır
# if __name__ == "__main__":
    create_tables()
    print("Tablolar başarıyla oluşturuldu!")