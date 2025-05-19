import customtkinter as ctk
from DB.Migrations.Teacher.create import ogretmen_ekle  # Bu senin ogretmen ekleme fonksiyonun
from DB.connection import get_connection

def ogretmen_ekleme_penceresi():
    win = ctk.CTkToplevel()
    win.title("Yeni Öğretmen Ekle")
    win.geometry("400x600")
    ogretmen_ekleme_sayfasi(win)
    win.lift()
    win.attributes('-topmost', True)
    win.after(200, lambda: win.attributes('-topmost', False))

def ogretmen_ekleme_sayfasi(root_frame):
    for widget in root_frame.winfo_children():
        widget.destroy()

    # Başlık
    title_label = ctk.CTkLabel(root_frame, text="Yeni Öğretmen Ekle", font=("Arial", 20, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

    # Öğretmen Adı
    ad_label = ctk.CTkLabel(root_frame, text="Adı:")
    ad_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    ad_entry = ctk.CTkEntry(root_frame)
    ad_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    # Öğretmen Soyadı
    soyad_label = ctk.CTkLabel(root_frame, text="Soyadı:")
    soyad_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

    soyad_entry = ctk.CTkEntry(root_frame)
    soyad_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    # Fotoğraf
    foto_label = ctk.CTkLabel(root_frame, text="Fotoğraf (URL):")
    foto_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")

    foto_entry = ctk.CTkEntry(root_frame)
    foto_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    # Adres
    adres_label = ctk.CTkLabel(root_frame, text="Adres:")
    adres_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")

    adres_entry = ctk.CTkEntry(root_frame)
    adres_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")

    # Telefon
    tel_label = ctk.CTkLabel(root_frame, text="Telefon No:")
    tel_label.grid(row=5, column=0, padx=10, pady=10, sticky="e")

    tel_entry = ctk.CTkEntry(root_frame)
    tel_entry.grid(row=5, column=1, padx=10, pady=10, sticky="w")

    # TCKN
    tckn_label = ctk.CTkLabel(root_frame, text="TCKN:")
    tckn_label.grid(row=6, column=0, padx=10, pady=10, sticky="e")

    tckn_entry = ctk.CTkEntry(root_frame)
    tckn_entry.grid(row=6, column=1, padx=10, pady=10, sticky="w")

    # Öğretmen Numarası
    numara_label = ctk.CTkLabel(root_frame, text="Öğretmen No:")
    numara_label.grid(row=7, column=0, padx=10, pady=10, sticky="e")

    numara_entry = ctk.CTkEntry(root_frame)
    numara_entry.grid(row=7, column=1, padx=10, pady=10, sticky="w")

    # Şifre
    sifre_label = ctk.CTkLabel(root_frame, text="Şifre:")
    sifre_label.grid(row=8, column=0, padx=10, pady=10, sticky="e")

    sifre_entry = ctk.CTkEntry(root_frame, show="*")
    sifre_entry.grid(row=8, column=1, padx=10, pady=10, sticky="w")

    # Kaydet Butonu
    def kaydet():
        ad = ad_entry.get()
        soyad = soyad_entry.get()
        foto = foto_entry.get()
        adres = adres_entry.get()
        tel = tel_entry.get()
        tckn = tckn_entry.get()
        numara = numara_entry.get()
        sifre = sifre_entry.get()

        # Öğretmen numarası ve telefon, tckn'yi integer olarak alıyoruz
        try:
            tel = int(tel)
            tckn = int(tckn)
            numara = int(numara)
        except ValueError:
            mesaj = ctk.CTkLabel(root_frame, text="Telefon, TCKN ve Öğretmen No sadece sayılar olmalı!", text_color="red")
            mesaj.grid(row=9, column=0, columnspan=2, pady=10)
            return

        # Önceki mesajları temizle
        for widget in root_frame.grid_slaves(row=9):
            widget.destroy()

        if ad and soyad and foto and adres and tel and tckn and numara and sifre:
            ogretmen_ekle(ad, soyad, foto, adres, tel, tckn, numara, sifre)
            mesaj = ctk.CTkLabel(root_frame, text="Öğretmen başarıyla eklendi!", text_color="green")

            ad_entry.delete(0, 'end')
            soyad_entry.delete(0, 'end')
            foto_entry.delete(0, 'end')
            adres_entry.delete(0, 'end')
            tel_entry.delete(0, 'end')
            tckn_entry.delete(0, 'end')
            numara_entry.delete(0, 'end')
            sifre_entry.delete(0, 'end')
        else:
            mesaj = ctk.CTkLabel(root_frame, text="Lütfen tüm alanları doldurun!", text_color="red")

        mesaj.grid(row=9, column=0, columnspan=2, pady=10)

    kaydet_button = ctk.CTkButton(root_frame, text="Kaydet", command=kaydet)
    kaydet_button.grid(row=10, column=0, columnspan=2, pady=20)

    # Grid kolonlarını eşitle
    root_frame.grid_columnconfigure(0, weight=1)
    root_frame.grid_columnconfigure(1, weight=1)
