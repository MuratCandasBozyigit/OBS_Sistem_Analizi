import customtkinter as ctk
from tkinter import messagebox
from DB.Migrations.ModelBuilder.TeacherCourse import (

    ogretmene_ders_ata,
    ogretmenin_derslerini_getir,
    ogretmene_ders_sil
)
from DB.Migrations.ModelBuilder.StudentCourse import(
        ogrenci_ders_ata,
    ogrencinin_derslerini_getir,
    ogrencinin_ders_sil,
)
from DB.Migrations.Class.read import tum_dersleri_getir
from DB.Migrations.Student import tum_ogrencileri_getir
from DB.Migrations.Teacher import tum_ogretmenleri_getir


def ders_ata_sayfasi():
    pencere = ctk.CTkToplevel()
    pencere.title("Ders Atama İşlemleri")
    pencere.geometry("400x300")

    ctk.CTkLabel(pencere, text="İşlem Seç", font=("Arial", 16)).pack(pady=20)

    ctk.CTkButton(pencere, text="Öğrenciye Ders Ata", command=ogrenci_ders_ata_penceresi).pack(pady=10)
    ctk.CTkButton(pencere, text="Öğretmene Ders Ata", command=ogretmen_ders_ata_penceresi).pack(pady=10)


def ogrenci_ders_ata_penceresi():
    pencere = ctk.CTkToplevel()
    pencere.title("Öğrenciye Ders Ata")
    pencere.geometry("400x500")

    try:
        ogrenciler = tum_ogrencileri_getir()
        dersler = tum_dersleri_getir()
    except Exception as e:
        messagebox.showerror("Hata", f"Veriler alınamadı:\n{e}")
        pencere.destroy()
        return

    secilen_ogrenci = ctk.StringVar()
    secilen_dersler = []

    ctk.CTkLabel(pencere, text="Öğrenci Seç:", font=("Arial", 14)).pack(pady=10)
    ogrenci_menu = ctk.CTkOptionMenu(pencere, variable=secilen_ogrenci,
                                     values=[f"{o[0]} - {o[1]} {o[2]}" for o in ogrenciler])
    ogrenci_menu.pack()

    ders_frame = ctk.CTkFrame(pencere)
    ders_frame.pack(pady=20)

    checkboxlar = []

    for ders in dersler:
        ders_id, ders_adi = ders
        var = ctk.BooleanVar()
        chk = ctk.CTkCheckBox(ders_frame, text=ders_adi, variable=var)
        chk.pack(anchor="w")
        checkboxlar.append((ders_id, var))

    def kaydet():
        try:
            ogrenci_id = int(secilen_ogrenci.get().split(" - ")[0])
            mevcut_dersler = {d[0] for d in ogrencinin_derslerini_getir(ogrenci_id)}

            eklendi = 0
            silindi = 0

            for ders_id, var in checkboxlar:
                if var.get() and ders_id not in mevcut_dersler:
                    ogrenci_ders_ata(ogrenci_id, ders_id)
                    eklendi += 1
                elif not var.get() and ders_id in mevcut_dersler:
                    ogrencinin_ders_sil(ogrenci_id, ders_id)
                    silindi += 1

            mesaj = []
            if eklendi: mesaj.append(f"{eklendi} ders eklendi.")
            if silindi: mesaj.append(f"{silindi} ders silindi.")
            if not mesaj: mesaj.append("Hiçbir değişiklik yapılmadı.")
            messagebox.showinfo("İşlem Tamamlandı", "\n".join(mesaj))
            pencere.destroy()
        except Exception as e:
            messagebox.showerror("Hata", f"Kaydetme sırasında hata oluştu:\n{e}")

    ctk.CTkButton(pencere, text="Kaydet", command=kaydet).pack(pady=10)


def ogretmen_ders_ata_penceresi():
    pencere = ctk.CTkToplevel()
    pencere.title("Öğretmene Ders Ata")
    pencere.geometry("400x500")

    try:
        ogretmenler = tum_ogretmenleri_getir()
        dersler = tum_dersleri_getir()
    except Exception as e:
        messagebox.showerror("Hata", f"Veriler alınamadı:\n{e}")
        pencere.destroy()
        return

    secilen_ogretmen = ctk.StringVar()
    checkboxlar = []

    ctk.CTkLabel(pencere, text="Öğretmen Seç:", font=("Arial", 14)).pack(pady=10)
    ogretmen_menu = ctk.CTkOptionMenu(pencere, variable=secilen_ogretmen,
                                      values=[f"{o[0]} - {o[1]} {o[2]}" for o in ogretmenler])
    ogretmen_menu.pack()

    ders_frame = ctk.CTkFrame(pencere)
    ders_frame.pack(pady=20)

    for ders in dersler:
        ders_id, ders_adi = ders
        var = ctk.BooleanVar()
        chk = ctk.CTkCheckBox(ders_frame, text=ders_adi, variable=var)
        chk.pack(anchor="w")
        checkboxlar.append((ders_id, var))

    def kaydet():
        try:
            ogretmen_id = int(secilen_ogretmen.get().split(" - ")[0])
            mevcut_dersler = {d[0] for d in ogretmenin_derslerini_getir(ogretmen_id)}

            eklendi = 0
            silindi = 0

            for ders_id, var in checkboxlar:
                if var.get() and ders_id not in mevcut_dersler:
                    ogretmene_ders_ata(ogretmen_id, ders_id)
                    eklendi += 1
                elif not var.get() and ders_id in mevcut_dersler:
                    ogretmene_ders_sil(ogretmen_id, ders_id)
                    silindi += 1

            mesaj = []
            if eklendi: mesaj.append(f"{eklendi} ders eklendi.")
            if silindi: mesaj.append(f"{silindi} ders silindi.")
            if not mesaj: mesaj.append("Hiçbir değişiklik yapılmadı.")
            messagebox.showinfo("İşlem Tamamlandı", "\n".join(mesaj))
            pencere.destroy()
        except Exception as e:
            messagebox.showerror("Hata", f"Kaydetme sırasında hata oluştu:\n{e}")

    ctk.CTkButton(pencere, text="Kaydet", command=kaydet).pack(pady=10)
