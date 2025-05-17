import customtkinter as ctk
from tkinter import messagebox
from DB.Migrations.Teacher import tum_ogretmenleri_getir
from DB.Migrations.ModelBuilder.TeacherStudent import (
    ogretmene_ogrenci_ata,
    ogretmenden_ogrenci_sil,
    ogrencinin_ogretmenlerini_getir
)

def ogretmen_ekle_ogrenci(ogrenci_id, parent=None):
    pencere = ctk.CTkToplevel()
    pencere.title("Öğretmen Ata")
    pencere.geometry("400x500")
    pencere.lift()
    pencere.attributes('-topmost', True)
    pencere.after(200, lambda: pencere.attributes('-topmost', False))
    ctk.CTkLabel(pencere, text="Öğretmen Seç:", font=("Arial", 16)).pack(pady=10)

    try:
        ogretmenler = tum_ogretmenleri_getir()
        ogrencinin_ogretmenleri = ogrencinin_ogretmenlerini_getir(ogrenci_id)
        atanmis_ogretmen_idler = {ogretmen[0] for ogretmen in ogrencinin_ogretmenleri}
    except Exception as e:
        messagebox.showerror("Hata", f"Öğretmenler alınamadı:\n{e}")
        pencere.destroy()
        return

    secilen_ogretmenler = []

    for ogretmen in ogretmenler:
        ogretmen_id = ogretmen[0]
        ogretmen_adi = ogretmen[1]
        ogretmen_soyadi = ogretmen[2]
        var = ctk.BooleanVar()

        if ogretmen_id in atanmis_ogretmen_idler:
            var.set(True)
            chk = ctk.CTkCheckBox(
                pencere,
                text=f"{ogretmen_adi} {ogretmen_soyadi}",
                variable=var,
                fg_color="green",
                hover_color="darkgreen"
            )
        else:
            chk = ctk.CTkCheckBox(
                pencere,
                text=f"{ogretmen_adi} {ogretmen_soyadi}",
                variable=var
            )

        chk.pack(anchor="w", padx=20)
        secilen_ogretmenler.append((ogretmen_id, var))

    def kaydet():
        eklendi = 0
        cikarildi = 0

        for ogretmen_id, var in secilen_ogretmenler:
            if var.get():
                if ogretmen_id not in atanmis_ogretmen_idler:
                    ogretmene_ogrenci_ata(ogretmen_id, ogrenci_id)
                    eklendi += 1
            else:
                if ogretmen_id in atanmis_ogretmen_idler:
                    ogretmenden_ogrenci_sil(ogretmen_id, ogrenci_id)
                    cikarildi += 1

        mesaj = []
        if eklendi > 0:
            mesaj.append(f"{eklendi} öğretmen atandı.")
        if cikarildi > 0:
            mesaj.append(f"{cikarildi} öğretmen çıkarıldı.")
        if not mesaj:
            mesaj.append("Hiçbir değişiklik yapılmadı.")

        messagebox.showinfo("İşlem Tamamlandı", "\n".join(mesaj))
        pencere.destroy()

    ctk.CTkButton(pencere, text="Kaydet", command=kaydet).pack(pady=20)
