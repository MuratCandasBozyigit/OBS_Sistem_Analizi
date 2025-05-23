﻿import customtkinter as ctk
from DB.Migrations.Student.create import ogrenci_ekle  # Bu fonksiyon DB işlemini yapan fonksiyon

def ogrenci_ekleme_penceresi():
    win = ctk.CTkToplevel()
    win.title("Yeni Öğrenci Ekle")
    win.geometry("400x500")  # Fotoğraf ve şifre alanı kaldırıldı, daha kısa bir pencere
    win.lift()
    win.attributes('-topmost', True)
    win.after(200, lambda: win.attributes('-topmost', False))
    
    ogrenci_ekleme_sayfasi(win)

def ogrenci_ekleme_sayfasi(root_frame):
    for widget in root_frame.winfo_children():
        widget.destroy()

    title_label = ctk.CTkLabel(root_frame, text="Yeni Öğrenci Ekle", font=("Arial", 20, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

    ogrenci_adi_label = ctk.CTkLabel(root_frame, text="Öğrenci Adı:")
    ogrenci_adi_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    ogrenci_adi_entry = ctk.CTkEntry(root_frame)
    ogrenci_adi_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    ogrenci_soyadi_label = ctk.CTkLabel(root_frame, text="Öğrenci Soyadı:")
    ogrenci_soyadi_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
    ogrenci_soyadi_entry = ctk.CTkEntry(root_frame)
    ogrenci_soyadi_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    ogrenci_tel_label = ctk.CTkLabel(root_frame, text="Öğrenci Telefon No:")
    ogrenci_tel_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")
    ogrenci_tel_entry = ctk.CTkEntry(root_frame)
    ogrenci_tel_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")

    ogrenci_tckn_label = ctk.CTkLabel(root_frame, text="Öğrenci TCKN:")
    ogrenci_tckn_label.grid(row=5, column=0, padx=10, pady=10, sticky="e")
    ogrenci_tckn_entry = ctk.CTkEntry(root_frame)
    ogrenci_tckn_entry.grid(row=5, column=1, padx=10, pady=10, sticky="w")

    ogrenci_numara_label = ctk.CTkLabel(root_frame, text="Öğrenci Numarası:")
    ogrenci_numara_label.grid(row=6, column=0, padx=10, pady=10, sticky="e")
    ogrenci_numara_entry = ctk.CTkEntry(root_frame)
    ogrenci_numara_entry.grid(row=6, column=1, padx=10, pady=10, sticky="w")

    def kaydet():
        ogrenci_adi = ogrenci_adi_entry.get().strip()
        ogrenci_soyadi = ogrenci_soyadi_entry.get().strip()
        ogrenci_tel = ogrenci_tel_entry.get().strip()
        ogrenci_tckn = ogrenci_tckn_entry.get().strip()
        ogrenci_numara = ogrenci_numara_entry.get().strip()

        for widget in root_frame.grid_slaves(row=7):
            widget.destroy()

        # Validasyon
        if not all([ogrenci_adi, ogrenci_soyadi, ogrenci_tel, ogrenci_tckn, ogrenci_numara]):
            mesaj = ctk.CTkLabel(root_frame, text="Lütfen tüm alanları doldurun!", text_color="red")
        elif not (ogrenci_tckn.isdigit() and len(ogrenci_tckn) == 11):
            mesaj = ctk.CTkLabel(root_frame, text="TCKN 11 haneli sayısal olmalıdır!", text_color="red")
        elif not (ogrenci_tel.isdigit() and len(ogrenci_tel) == 11 and ogrenci_tel.startswith("0")):
            mesaj = ctk.CTkLabel(root_frame, text="Telefon 0 ile başlamalı ve 11 haneli olmalıdır!", text_color="red")
        elif not ogrenci_numara.isdigit():
            mesaj = ctk.CTkLabel(root_frame, text="Öğrenci numarası sayısal olmalıdır!", text_color="red")
        else:
            ogrenci_ekle(ogrenci_adi, ogrenci_soyadi, ogrenci_tel, ogrenci_tckn, ogrenci_numara)  # Fotoğraf ve şifre boş bırakıldı
            mesaj = ctk.CTkLabel(root_frame, text="Öğrenci başarıyla eklendi!", text_color="green")
            ogrenci_adi_entry.delete(0, 'end')
            ogrenci_soyadi_entry.delete(0, 'end')
            ogrenci_tel_entry.delete(0, 'end')
            ogrenci_tckn_entry.delete(0, 'end')
            ogrenci_numara_entry.delete(0, 'end')

        mesaj.grid(row=7, column=0, columnspan=2, pady=10)

    kaydet_button = ctk.CTkButton(root_frame, text="Kaydet", command=kaydet)
    kaydet_button.grid(row=8, column=0, columnspan=2, pady=20)

    root_frame.grid_columnconfigure(0, weight=1)
    root_frame.grid_columnconfigure(1, weight=1)
