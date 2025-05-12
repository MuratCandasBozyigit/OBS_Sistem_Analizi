import sqlite3
import os

DB_PATH = os.path.join(os.getcwd(), "okul.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute('''
    INSERT INTO adminler (ad_sooyad, kullanici_adi, sifre)
    VALUES (?,  ?, ?)
''', ("murat",  "murat", "9212"))

conn.commit()
conn.close()

