import customtkinter as ctk
from DB.Migrations.Student.create import ogrenci_ekle  # Bu fonksiyon DB işlemini yapan fonksiyon

def ogrenci_ekleme_penceresi():
    win = ctk.CTkToplevel()
    win.title("Yeni Öğrenci Ekle")
    win.geometry("400x400")
    ogrenci_ekleme_sayfasi(win)

def ogrenci_ekleme_sayfasi(root_frame):
    for widget in root_frame.winfo_children():
        widget.destroy()

    # Başlık
    title_label = ctk.CTkLabel(root_frame, text="Yeni Öğrenci Ekle", font=("Arial", 20, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

    # Öğrenci Adı
    ogrenci_adi_label = ctk.CTkLabel(root_frame, text="Öğrenci Adı:")
    ogrenci_adi_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    ogrenci_adi_entry = ctk.CTkEntry(root_frame)
    ogrenci_adi_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    # Öğrenci Soyadı
    ogrenci_soyadi_label = ctk.CTkLabel(root_frame, text="Öğrenci Soyadı:")
    ogrenci_soyadi_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

    ogrenci_soyadi_entry = ctk.CTkEntry(root_frame)
    ogrenci_soyadi_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    # Öğrenci Fotoğrafı
    ogrenci_foto_label = ctk.CTkLabel(root_frame, text="Öğrenci Fotoğrafı (URL):")
    ogrenci_foto_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")

    ogrenci_foto_entry = ctk.CTkEntry(root_frame)
    ogrenci_foto_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    # Öğrenci Adresi
    ogrenci_adres_label = ctk.CTkLabel(root_frame, text="Öğrenci Adresi:")
    ogrenci_adres_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")

    ogrenci_adres_entry = ctk.CTkEntry(root_frame)
    ogrenci_adres_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")

    # Öğrenci Telefon Numarası
    ogrenci_tel_label = ctk.CTkLabel(root_frame, text="Öğrenci Telefon No:")
    ogrenci_tel_label.grid(row=5, column=0, padx=10, pady=10, sticky="e")

    ogrenci_tel_entry = ctk.CTkEntry(root_frame)
    ogrenci_tel_entry.grid(row=5, column=1, padx=10, pady=10, sticky="w")

    # Öğrenci TCKN
    ogrenci_tckn_label = ctk.CTkLabel(root_frame, text="Öğrenci TCKN:")
    ogrenci_tckn_label.grid(row=6, column=0, padx=10, pady=10, sticky="e")

    ogrenci_tckn_entry = ctk.CTkEntry(root_frame)
    ogrenci_tckn_entry.grid(row=6, column=1, padx=10, pady=10, sticky="w")

    # Öğrenci Numarası
    ogrenci_numara_label = ctk.CTkLabel(root_frame, text="Öğrenci Numarası:")
    ogrenci_numara_label.grid(row=7, column=0, padx=10, pady=10, sticky="e")

    ogrenci_numara_entry = ctk.CTkEntry(root_frame)
    ogrenci_numara_entry.grid(row=7, column=1, padx=10, pady=10, sticky="w")

    # Şifre
    sifre_label = ctk.CTkLabel(root_frame, text="Şifre:")
    sifre_label.grid(row=8, column=0, padx=10, pady=10, sticky="e")

    sifre_entry = ctk.CTkEntry(root_frame, show="*")
    sifre_entry.grid(row=8, column=1, padx=10, pady=10, sticky="w")

    # Kaydet Butonu
    def kaydet():
        ogrenci_adi = ogrenci_adi_entry.get()
        ogrenci_soyadi = ogrenci_soyadi_entry.get()
        ogrenci_foto = ogrenci_foto_entry.get()
        ogrenci_adres = ogrenci_adres_entry.get()
        ogrenci_tel = ogrenci_tel_entry.get()
        ogrenci_tckn = ogrenci_tckn_entry.get()
        ogrenci_numara = ogrenci_numara_entry.get()
        sifre = sifre_entry.get()

        # Önceki mesajları temizle
        for widget in root_frame.grid_slaves(row=9):
            widget.destroy()

        if ogrenci_adi and ogrenci_soyadi and ogrenci_foto and ogrenci_adres and ogrenci_tel and ogrenci_tckn and ogrenci_numara and sifre:
            ogrenci_ekle(ogrenci_adi, ogrenci_soyadi, ogrenci_foto, ogrenci_adres, ogrenci_tel, ogrenci_tckn, ogrenci_numara, sifre)
            mesaj = ctk.CTkLabel(root_frame, text="Öğrenci başarıyla eklendi!", text_color="green")
            ogrenci_adi_entry.delete(0, 'end')
            ogrenci_soyadi_entry.delete(0, 'end')
            ogrenci_foto_entry.delete(0, 'end')
            ogrenci_adres_entry.delete(0, 'end')
            ogrenci_tel_entry.delete(0, 'end')
            ogrenci_tckn_entry.delete(0, 'end')
            ogrenci_numara_entry.delete(0, 'end')
            sifre_entry.delete(0, 'end')
        else:
            mesaj = ctk.CTkLabel(root_frame, text="Lütfen tüm alanları doldurun!", text_color="red")

        mesaj.grid(row=9, column=0, columnspan=2, pady=10)

    kaydet_button = ctk.CTkButton(root_frame, text="Kaydet", command=kaydet)
    kaydet_button.grid(row=8, column=0, columnspan=2, pady=20)

    # Grid kolonlarını eşitle
    root_frame.grid_columnconfigure(0, weight=1)
    root_frame.grid_columnconfigure(1, weight=1)
