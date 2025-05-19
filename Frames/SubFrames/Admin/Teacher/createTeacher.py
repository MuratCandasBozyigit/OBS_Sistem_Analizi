import customtkinter as ctk
from DB.Migrations.Teacher.create import ogretmen_ekle

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

    title_label = ctk.CTkLabel(root_frame, text="Yeni Öğretmen Ekle", font=("Arial", 20, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

    ad_label = ctk.CTkLabel(root_frame, text="Adı:")
    ad_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    ad_entry = ctk.CTkEntry(root_frame)
    ad_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    soyad_label = ctk.CTkLabel(root_frame, text="Soyadı:")
    soyad_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
    soyad_entry = ctk.CTkEntry(root_frame)
    soyad_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")



    adres_label = ctk.CTkLabel(root_frame, text="Adres:")
    adres_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")
    adres_entry = ctk.CTkEntry(root_frame)
    adres_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")

    tel_label = ctk.CTkLabel(root_frame, text="Telefon No:")
    tel_label.grid(row=5, column=0, padx=10, pady=10, sticky="e")
    tel_entry = ctk.CTkEntry(root_frame)
    tel_entry.grid(row=5, column=1, padx=10, pady=10, sticky="w")

    tckn_label = ctk.CTkLabel(root_frame, text="TCKN:")
    tckn_label.grid(row=6, column=0, padx=10, pady=10, sticky="e")
    tckn_entry = ctk.CTkEntry(root_frame)
    tckn_entry.grid(row=6, column=1, padx=10, pady=10, sticky="w")

    numara_label = ctk.CTkLabel(root_frame, text="Öğretmen No:")
    numara_label.grid(row=7, column=0, padx=10, pady=10, sticky="e")
    numara_entry = ctk.CTkEntry(root_frame)
    numara_entry.grid(row=7, column=1, padx=10, pady=10, sticky="w")



    def reset_entry_styles():
        ad_entry.configure(border_color="gray")
        soyad_entry.configure(border_color="gray")
        adres_entry.configure(border_color="gray")
        tel_entry.configure(border_color="gray")
        tckn_entry.configure(border_color="gray")
        numara_entry.configure(border_color="gray")

    def kaydet():
        reset_entry_styles()
        ad = ad_entry.get()
        soyad = soyad_entry.get()
        adres = adres_entry.get()
        tel = tel_entry.get()
        tckn = tckn_entry.get()
        numara = numara_entry.get()

        for widget in root_frame.grid_slaves(row=9):
            widget.destroy()

        valid = True

        if not ad: ad_entry.configure(border_color="red"); valid = False
        if not soyad: soyad_entry.configure(border_color="red"); valid = False
        if not adres: adres_entry.configure(border_color="red"); valid = False

        # Telefon: +90 ile başlamalı ve 13 haneli olmalı
        if not tel.startswith("0") or len(tel) != 11 or not tel[3:].isdigit():
            tel_entry.configure(border_color="red")
            valid = False

        # TCKN: 11 haneli ve sadece rakam
        if len(tckn) != 11 or not tckn.isdigit():
            tckn_entry.configure(border_color="red")
            valid = False

        # Öğretmen No: 1-9 hane ve sadece rakam
        if not numara.isdigit() or not (1 <= len(numara) <= 9):
            numara_entry.configure(border_color="red")
            valid = False

        if valid:
            ogretmen_ekle(ad, soyad,  adres, int(tel[3:]), int(tckn), int(numara))
            mesaj = ctk.CTkLabel(root_frame, text="Öğretmen başarıyla eklendi!", text_color="green")

            ad_entry.delete(0, 'end')
            soyad_entry.delete(0, 'end')
            adres_entry.delete(0, 'end')
            tel_entry.delete(0, 'end')
            tckn_entry.delete(0, 'end')
            numara_entry.delete(0, 'end')
        else:
            mesaj = ctk.CTkLabel(root_frame, text="Lütfen geçerli bilgileri girin!", text_color="red")

        mesaj.grid(row=9, column=0, columnspan=2, pady=10)

    kaydet_button = ctk.CTkButton(root_frame, text="Kaydet", command=kaydet)
    kaydet_button.grid(row=10, column=0, columnspan=2, pady=20)

    root_frame.grid_columnconfigure(0, weight=1)
    root_frame.grid_columnconfigure(1, weight=1)
