import sqlite3
import os



DB_PATH = os.path.join(os.getcwd(), "okul.db")

def get_connection():
    return sqlite3.connect(DB_PATH)


def init_database():
    import DB.Migrations
    DB.Migrations.create_dersler_table()
    DB.Migrations.create_ogrenciler_table()
    DB.Migrations.create_ogretmenler_table()
    DB.Migrations.create_adminler_table()
    DB.Migrations.create_ogretmen_ders_table()
    DB.Migrations.create_ogretmen_ogrenci_table()
    DB.Migrations.create_ogrenci_ders_table()
    DB.Migrations.create_notlar_table()
    
    