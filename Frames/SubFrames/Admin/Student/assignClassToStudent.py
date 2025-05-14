import customtkinter as ctk
from tkinter import messagebox
from functools import partial
from DB.Migrations.Class import tum_dersleri_getir
from DB.Migrations.ModelBuilder.StudentCourse import (
    ogrenci_ders_ata, ogrencinin_ders_sil, ogrencinin_derslerini_getir
)

def ders_ekle_ogrenci(ogrenci_id, parent=None):
    pencere = ctk.CTkToplevel()
    pencere.title("Ders Ata")
    pencere.geometry("400x500")
    
    ctk.CTkLabel(pencere, text="Ders Seç:", font=("Arial", 16)).pack(pady=10)

    try:
        dersler = tum_dersleri_getir() 
        ogrencin_dersleri = ogrencinin_derslerini_getir(ogrenci_id)  
        atanmis_ders_idler = {ders_id for ders_id, _ in ogrencin_dersleri}
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
                fg_color="green",  
                hover_color="darkgreen"
            )
        else:
            chk = ctk.CTkCheckBox(pencere, text=ders_adi, variable=var)

        chk.pack(anchor="w", padx=20)
        secilen_dersler.append((ders_id, var))

        # Ders kaldırılırsa anında sil
        def uncheck_ders(ders_id, var):
            if not var.get():
                try:
                    ogrencinin_ders_sil(ogrenci_id, ders_id)
                except Exception as e:
                    messagebox.showerror("Silme Hatası", f"{ders_id} dersi silinemedi:\n{e}")

        chk.configure(command=partial(uncheck_ders, ders_id, var))

    def kaydet():
        eklendi = 0
        for ders_id, var in secilen_dersler:
            if var.get() and ders_id not in atanmis_ders_idler:
                try:
                    ogrenci_ders_ata(ogrenci_id, ders_id)
                    eklendi += 1
                except Exception as e:
                    messagebox.showerror("Hata", f"{ders_id} atanamadı:\n{e}")

        if eklendi > 0:
            messagebox.showinfo("Başarılı", f"{eklendi} ders atandı.")
        else:
            messagebox.showinfo("Bilgi", "Yeni ders atanmadı.")
        
        pencere.destroy()

    ctk.CTkButton(pencere, text="Kaydet", command=kaydet).pack(pady=20)
