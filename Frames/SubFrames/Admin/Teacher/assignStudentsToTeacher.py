import customtkinter as ctk
from tkinter import messagebox
from DB.Migrations.Student import tum_ogrencileri_getir
from DB.Migrations.ModelBuilder.TeacherStudent import (
    ogretmene_ogrenci_ata,
    ogretmenden_ogrenci_sil,
    ogrencinin_ogretmenlerini_getir,
    ogretmenin_ogrencilerini_getir
)

def ogrenci_ekle_ogretmen(ogretmen_id, parent=None):
    pencere = ctk.CTkToplevel()
    pencere.title("Öğrenci Ekle")
    pencere.geometry("400x500")
    pencere.lift()
    pencere.attributes('-topmost', True)
    pencere.after(200, lambda: pencere.attributes('-topmost', False))
    ctk.CTkLabel(pencere, text="Öğrenci Seç:", font=("Arial", 16)).pack(pady=10)

    try:
        ogrenciler = tum_ogrencileri_getir()
        ogretmenin_ogrencileri = ogretmenin_ogrencilerini_getir(ogretmen_id)
        atanmis_ogrenci_idler = {ogrenci[0] for ogrenci in ogretmenin_ogrencileri}
    except Exception as e:
        messagebox.showerror("Hata", f"Öğrenciler alınamadı:\n{e}")
        pencere.destroy()
        return

    secilen_ogrenciler = []

    for ogrenci in ogrenciler:
        ogrenci_id = ogrenci[0]
        ogrenci_adi = ogrenci[1]
        ogrenci_soyadi = ogrenci[2]
        var = ctk.BooleanVar()

        if ogrenci_id in atanmis_ogrenci_idler:
            var.set(True)
            chk = ctk.CTkCheckBox(
                pencere,
                text=ogrenci_adi + " " + ogrenci_soyadi,
                variable=var,
                fg_color="green",
                hover_color="darkgreen"
            )
        else:
            chk = ctk.CTkCheckBox(
                pencere,
                text=ogrenci_adi + " " + ogrenci_soyadi,
                variable=var
            )

        chk.pack(anchor="w", padx=20)
        secilen_ogrenciler.append((ogrenci_id, var))

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
                    ogretmenden_ogrenci_sil(ogretmen_id, ogrenci_id)
                    cikarildi += 1

        mesaj = []
        if eklendi > 0:
            mesaj.append(f"{eklendi} öğrenci eklendi.")
        if cikarildi > 0:
            mesaj.append(f"{cikarildi} öğrenci çıkarıldı.")
        if not mesaj:
            mesaj.append("Hiçbir değişiklik yapılmadı.")

        messagebox.showinfo("İşlem Tamamlandı", "\n".join(mesaj))
        pencere.destroy()

    ctk.CTkButton(pencere, text="Kaydet", command=kaydet).pack(pady=20)
