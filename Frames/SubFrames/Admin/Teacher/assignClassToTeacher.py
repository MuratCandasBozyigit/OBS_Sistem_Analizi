# assignClassToTeacher.py

import customtkinter as ctk
from tkinter import messagebox
from DB.Migrations.Class import tum_dersleri_getir
from DB.Migrations.ModelBuilder.TeacherCourse import (
    ogretmene_ders_ata,
    ogretmenin_derslerini_getir
)

def ders_ekle_ogretmen(ogretmen_id, parent=None):
    pencere = ctk.CTkToplevel()
    pencere.title("Ders Ata")
    pencere.geometry("400x500")
    
    ctk.CTkLabel(pencere, text="Ders Seç:", font=("Arial", 16)).pack(pady=10)

    try:
        dersler = tum_dersleri_getir()  # [(ders_id, ders_adi, ders_saati, ...)]
        ogretmenin_dersleri = ogretmenin_derslerini_getir(ogretmen_id)  # [(ders_id, ders_adi)]
        atanmis_ders_idler = {ders_id for ders_id, _ in ogretmenin_dersleri}
    except Exception as e:
        messagebox.showerror("Hata", f"Dersler alınamadı:\n{e}")
        pencere.destroy()
        return

    secilen_dersler = []

    for ders in dersler:
        ders_id = ders[0]
        ders_adi = ders[1]
        var = ctk.BooleanVar()

        if ders_id in atanmis_ders_idler:
            var.set(True)
            chk = ctk.CTkCheckBox(
                pencere,
                text=ders_adi,
                variable=var,
                fg_color="green",  # Tik kutusunun iç rengi
                hover_color="darkgreen"
            )
        else:
            chk = ctk.CTkCheckBox(pencere, text=ders_adi, variable=var)

        chk.pack(anchor="w", padx=20)
        secilen_dersler.append((ders_id, var))

    def kaydet():
        eklendi = 0
        for ders_id, var in secilen_dersler:
            if var.get():
                ogretmene_ders_ata(ogretmen_id, ders_id)
                eklendi += 1

        if eklendi > 0:
            messagebox.showinfo("Başarılı", f"{eklendi} ders atandı.")
        else:
            messagebox.showwarning("Uyarı", "Hiçbir ders seçilmedi.")
        
        pencere.destroy()

    ctk.CTkButton(pencere, text="Kaydet", command=kaydet).pack(pady=20)
