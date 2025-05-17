import customtkinter as ctk
from DB.Migrations.ModelBuilder.StudentCourse import ogrencinin_derslerini_getir

def DersListesiSayfasi(parent_frame, ogrenci_id):
    """
    Bu fonksiyon verilen parent_frame içine ders listesini bir sayfa olarak ekler.
    """
    for widget in parent_frame.winfo_children():
        widget.destroy()

    title = ctk.CTkLabel(parent_frame, text="Aldığınız Dersler:", font=("Arial", 18))
    title.pack(pady=20)

    dersler = ogrencinin_derslerini_getir(ogrenci_id)
    if dersler:
        for ders_id, ders_adı in dersler:
            ctk.CTkLabel(parent_frame, text=f"• {ders_adı}", font=("Arial", 14)).pack(anchor="w", padx=30, pady=5)
    else:
        ctk.CTkLabel(parent_frame, text="Ders bulunamadı.", font=("Arial", 14), text_color="red").pack(pady=10)
