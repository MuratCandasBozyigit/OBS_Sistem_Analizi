import customtkinter as ctk
from DB.Migrations.Student.create import ogrenci_ekle  # Bu fonksiyon DB işlemini yapan fonksiyon

def ogrenci_ekleme_penceresi():
    win = ctk.CTkToplevel()
    win.title("Yeni Öğrenci Ekle")
    win.geometry("400x600")
    win.lift()
    win.attributes('-topmost', True)
    win.after(200, lambda: win.attributes('-topmost', False))
    
    ogrenci_ekleme_sayfasi(win)

def ogrenci_ekleme_sayfasi(root_frame):
    for widget in root_frame.winfo_children():
        widget.destroy()

    title_label = ctk.CTkLabel(root_frame, text="Yeni Öğrenci Ekle", font=("Arial", 20, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

    # Öğrenci adı
    ogrenci_adi_label = ctk.CTkLabel(root_frame, text="Öğrenci Adı:")
    ogrenci_adi_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    ogrenci_adi_entry = ctk.CTkEntry(root_frame)
    ogrenci_adi_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    # Öğrenci soyadı
    ogrenci_soyadi_label = ctk.CTkLabel(root_frame, text="Öğrenci Soyadı:")
    ogrenci_soyadi_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
    ogrenci_soyadi_entry = ctk.CTkEntry(root_frame)
    ogrenci_soyadi_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    # Öğrenci fotoğrafı (URL)
    ogrenci_foto_label = ctk.CTkLabel(root_frame, text="Öğrenci Fotoğrafı (URL):")
    ogrenci_foto_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
    ogrenci_foto_entry = ctk.CTkEntry(root_frame)
    ogrenci_foto_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    # Öğrenci adresi
    ogrenci_adres_label = ctk.CTkLabel(root_frame, text="Öğrenci Adresi:")
    ogrenci_adres_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")
    ogrenci_adres_entry = ctk.CTkEntry(root_frame)
    ogrenci_adres_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")

    # Öğrenci telefon numarası
    ogrenci_tel_label = ctk.CTkLabel(root_frame, text="Öğrenci Telefon No:")
    ogrenci_tel_label.grid(row=5, column=0, padx=10, pady=10, sticky="e")
    ogrenci_tel_entry = ctk.CTkEntry(root_frame)
    ogrenci_tel_entry.grid(row=5, column=1, padx=10, pady=10, sticky="w")

    # Öğrenci TCKN
    ogrenci_tckn_label = ctk.CTkLabel(root_frame, text="Öğrenci TCKN:")
    ogrenci_tckn_label.grid(row=6, column=0, padx=10, pady=10, sticky="e")
    ogrenci_tckn_entry = ctk.CTkEntry(root_frame)
    ogrenci_tckn_entry.grid(row=6, column=1, padx=10, pady=10, sticky="w")

    # Öğrenci numarası
    ogrenci_numara_label = ctk.CTkLabel(root_frame, text="Öğrenci Numarası:")
    ogrenci_numara_label.grid(row=7, column=0, padx=10, pady=10, sticky="e")
    ogrenci_numara_entry = ctk.CTkEntry(root_frame)
    ogrenci_numara_entry.grid(row=7, column=1, padx=10, pady=10, sticky="w")

    # Şifre
    sifre_label = ctk.CTkLabel(root_frame, text="Şifre:")
    sifre_label.grid(row=8, column=0, padx=10, pady=10, sticky="e")
    sifre_entry = ctk.CTkEntry(root_frame, show="*")
    sifre_entry.grid(row=8, column=1, padx=10, pady=10, sticky="w")

    def kaydet():
        # Kullanıcıdan alınan veriler
        ogrenci_adi = ogrenci_adi_entry.get()
        ogrenci_soyadi = ogrenci_soyadi_entry.get()
        ogrenci_foto = ogrenci_foto_entry.get()
        ogrenci_adres = ogrenci_adres_entry.get()
        ogrenci_tel = ogrenci_tel_entry.get()
        ogrenci_tckn = ogrenci_tckn_entry.get()
        ogrenci_numara = ogrenci_numara_entry.get()
        sifre = sifre_entry.get()

        valid = True  # Tüm alanların geçerli olduğunu varsayalım

        # Hatalı girişlerin kontrolü
        if not ogrenci_adi:
            ogrenci_adi_entry.configure(border_color="red")
            valid = False
        if not ogrenci_soyadi:
            ogrenci_soyadi_entry.configure(border_color="red")
            valid = False
        if not ogrenci_foto:
            ogrenci_foto_entry.configure(border_color="red")
            valid = False
        if not ogrenci_adres:
            ogrenci_adres_entry.configure(border_color="red")
            valid = False
        if not ogrenci_tel or len(ogrenci_tel) != 10 or not ogrenci_tel.isdigit():
            ogrenci_tel_entry.configure(border_color="red")
            valid = False
        if not ogrenci_tckn or len(ogrenci_tckn) != 11 or not ogrenci_tckn.isdigit():
            ogrenci_tckn_entry.configure(border_color="red")
            valid = False
        if not ogrenci_numara or not ogrenci_numara.isdigit():
            ogrenci_numara_entry.configure(border_color="red")
            valid = False
        if not sifre:
            sifre_entry.configure(border_color="red")
            valid = False

        if valid:
            # Veritabanına ekleme işlemi
            ogrenci_ekle(
                ogrenci_adi,
                ogrenci_soyadi,
                ogrenci_foto,
                ogrenci_adres,
                ogrenci_tel,
                ogrenci_tckn,
                ogrenci_numara,
                sifre
            )

            mesaj = ctk.CTkLabel(root_frame, text="Öğrenci başarıyla eklendi!", text_color="green")
            # Alanları temizle
            ogrenci_adi_entry.delete(0, 'end')
            ogrenci_soyadi_entry.delete(0, 'end')
            ogrenci_foto_entry.delete(0, 'end')
            ogrenci_adres_entry.delete(0, 'end')
            ogrenci_tel_entry.delete(0, 'end')
            ogrenci_tckn_entry.delete(0, 'end')
            ogrenci_numara_entry.delete(0, 'end')
            sifre_entry.delete(0, 'end')
        else:
            mesaj = ctk.CTkLabel(root_frame, text="Lütfen tüm alanları doğru şekilde doldurun!", text_color="red")

        mesaj.grid(row=9, column=0, columnspan=2, pady=10)

    kaydet_button = ctk.CTkButton(root_frame, text="Kaydet", command=kaydet)
    kaydet_button.grid(row=10, column=0, pady=20)

    iptal_button = ctk.CTkButton(root_frame, text="İptal", command=root_frame.destroy)
    iptal_button.grid(row=10, column=1, pady=20)

    root_frame.grid_columnconfigure(0, weight=1)
    root_frame.grid_columnconfigure(1, weight=1)
