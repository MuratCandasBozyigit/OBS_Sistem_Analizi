#Bir oğretmen 30 ogrenci var diyleim mantıken otuz ogrenciye tıklayıp tek tek ogretmen atamak yerine öğretmene tıklarım ogrencileri listelerim
#listlediğim ogrencileri checkbox ile seçerim seçtiklerimi 

import customtkinter as ctk
from tkinter import messagebox
from DB.Migrations.Student import tum_ogrencileri_getir
from DB.Migrations.ModelBuilder.TeacherStudent import (
  ogretmene_ogrenci_ata,
  ogretmene_ogrencilerini_sil,
  ogretmenin_ogrencilerini_getir
)

def ogrenci_ekle_ogretmen(ogretmen_id, parent=None):
    pencere = ctk.CTkToplevel()
    pencere.title("Öğrenci Ekle")
    pencere.geometry("400x500")
    
    ctk.CTkLabel(pencere, text="Öğrenci Seç:", font=("Arial", 16)).pack(pady=10)

    try:
        ogrenciler = tum_ogrencileri_getir() 
        ogretmenin_ogrencileri = ogretmenin_ogrencilerini_getir(ogretmen_id)  
        atanmis_ogrenci_idler = {ogrenci[0] for ogrenci in ogretmenin_ogrencileri}
        # atanmis_ogrenci_idler = {ogrenci_id for ogrenci_id, _ in ogretmenin_ogrencileri}
    except Exception as e:
        messagebox.showerror("Hata", f"Öğrenciler alınamadı:\n{e}")
        pencere.destroy()
        return

    secilen_ogrenciler = []

    for ogrenci in ogrenciler:
        ogrenci_id = ogrenci[0]
        ogrenci_adi = ogrenci[1]
        ogrenci_soyadı =ogrenci[2]
        var = ctk.BooleanVar()

        if ogrenci_id in atanmis_ogrenci_idler:
            var.set(True)
            chk = ctk.CTkCheckBox(
                pencere,
                text=ogrenci_adi+ogrenci_soyadı,
                variable=var,
                fg_color="green",  
                hover_color="darkgreen"
            )
        else:
            chk = ctk.CTkCheckBox(pencere, text=ogrenci_adi+ogrenci_soyadı, variable=var)

        chk.pack(anchor="w", padx=20)
        secilen_ogrenciler.append((ogrenci_id, var))

        def uncheck_ogrenci(ogrenci_id, var):
            if not var.get():
                ogretmene_ogrencilerini_sil(ogretmen_id, ogrenci_id)

        chk.configure(command=lambda ogrenci_id=ogrenci_id, var=var: uncheck_ogrenci(ogrenci_id, var))

    def kaydet():
        eklendi = 0
        cikarildi = 0

        for ogrenci_id, var in secilen_ogrenciler:
            if var.get():
                if ogrenci_id not in atanmis_ogrenci_idler:
                    ogretmene_ogrenci_ata(ogretmen_id, ogrenci_id)
                    eklendi += 1
            else:
                if ogrenci_id in atanmis_ogrenci_idler:
                    ogretmene_ogrencilerini_sil(ogretmen_id, ogrenci_id)
                    cikarildi += 1

        mesaj = []
        if eklendi > 0:
            mesaj.append(f"{eklendi} öğrenci **eklendi**.")
        if cikarildi > 0:
            mesaj.append(f"{cikarildi} öğrenci **çıkarıldı**.")
        if not mesaj:
            mesaj.append("Hiçbir değişiklik yapılmadı.")

        messagebox.showinfo("İşlem Tamamlandı", "\n".join(mesaj))
        pencere.destroy()

        eklendi = 0
        for ogrenci_id, var in secilen_ogrenciler:
            if var.get():
                ogretmene_ogrenci_ata(ogretmen_id, ogrenci_id)
                eklendi += 1

            if eklendi > 0:
                messagebox.showinfo("Başarılı", f"{eklendi} öğrenci eklendi.")
            elif eklendi < 0:
                messagebox.showinfo("Başarılı",f"{eklendi} ogrenci çıkarıldı.")
            else:
                messagebox.showwarning("Uyarı", "Hiçbir öğrenci seçilmedi.")
            
            pencere.destroy()

    ctk.CTkButton(pencere, text="Kaydet", command=kaydet).pack(pady=20)
