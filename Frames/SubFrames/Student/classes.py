import customtkinter as ctk
from DB.Migrations.ModelBuilder.StudentCourse import ogrencinin_derslerini_getir

def DersListesiSayfasi():
   print("Ders Listesi Sayfası Açılıyor...")
   dersler = ogrencinin_derslerini_getir(1)  # Örnek olarak 1. ID'li öğrencinin derslerini alıyoruz