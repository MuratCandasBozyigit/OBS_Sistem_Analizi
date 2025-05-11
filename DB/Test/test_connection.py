from connection import get_connection

def test_db_connection():
    connection = get_connection()
    if connection:
        print("Veritabanına bağlanıldı!")
    else:
        print("Bağlantı hatası!")

if __name__ == "__main__":
    test_db_connection()
