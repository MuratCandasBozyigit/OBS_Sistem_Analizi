#ogretmen seç tuşa bas dersler listelensin ve dersi seç tada sonra kaydete bas ders veya dersleri seçmen lazım ,
# çok ii lan boyle kendime not almak mantıklı ha obsidian kadar bu da iş yapıyor 

#GetTeacher.py dan buton ile bu sayfaya yonlendirme yap ardından bu yonlendirme ile bilrikte pencere açılır açılan pencerede ekleme işlmeini yaparsın
#az mola vereceğim ondan kendime notlar alıyorums 

import customtkinter as ctk
from tkinter import messagebox
from DB.Migrations.Class import tum_dersleri_getir
from DB.Migrations.ModelBuilder.TeacherCourse import ogretmene_ders_ata

def ders_ekle_ogretmen(ogretmen_id, parent):
    pencere = ctk.CTkToplevel()
    pencere.title("Ders Ata")
    pencere.geometry("400x400")

    ctk.CTkLabel(pencere, text="Ders Seç:", font=("Arial", 16)).pack(pady=10)

    dersler = tum_dersleri_getir()
    secilen_dersler = []

    for ders_id, ders_adi in dersler:
        var = ctk.BooleanVar()
        chk = ctk.CTkCheckBox(pencere, text=ders_adi, variable=var)
        chk.pack(anchor="w", padx=20)
        secilen_dersler.append((ders_id, var))

    def kaydet():
        eklendi = 0
        for ders_id, var in secilen_dersler:
            if var.get():
                ogretmene_ders_ata(ogretmen_id, ders_id)
                eklendi += 1
        if eklendi:
            messagebox.showinfo("Başarılı", f"{eklendi} ders atandı.")
        else:
            messagebox.showwarning("Uyarı", "Hiçbir ders seçilmedi.")
        pencere.destroy()

    ctk.CTkButton(pencere, text="Kaydet", command=kaydet).pack(pady=20)
