import sqlite3
import os

DB_PATH = os.path.join(os.getcwd(), "okul.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute('''
    INSERT INTO adminler (ad_soyad, kullanici_adi, sifre)
    VALUES (?,  ?, ?)
''', ("w",  "w", "w"))

conn.commit()
conn.close()

