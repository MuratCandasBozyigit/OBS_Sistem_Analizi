import customtkinter as ctk
from DB.Migrations.Class.create import ders_ekle  # Bu fonksiyon senin DB işlemini yapan fonksiyon

def ders_ekleme_penceresi():
    win = ctk.CTkToplevel()
    win.title("Yeni Ders Ekle")
    win.geometry("400x300")
    ders_ekleme_sayfasi(win)

def ders_ekleme_sayfasi(root_frame):
    for widget in root_frame.winfo_children():
        widget.destroy()

    # Başlık
    title_label = ctk.CTkLabel(root_frame, text="Yeni Ders Ekle", font=("Arial", 20, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

    # Ders Adı
    ders_adi_label = ctk.CTkLabel(root_frame, text="Ders Adı:")
    ders_adi_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    ders_adi_entry = ctk.CTkEntry(root_frame)
    ders_adi_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    # Ders Saati
    ders_saati_label = ctk.CTkLabel(root_frame, text="Ders Saati:")
    ders_saati_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

    ders_saati_entry = ctk.CTkEntry(root_frame)
    ders_saati_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    # Kaydet Butonu
    def kaydet():
        ders_adi = ders_adi_entry.get()
        ders_saati = ders_saati_entry.get()

        # Önceki mesajları temizle
        for widget in root_frame.grid_slaves(row=4):
            widget.destroy()

        if ders_adi and ders_saati:
            ders_ekle(ders_adi, ders_saati)
            mesaj = ctk.CTkLabel(root_frame, text="Ders başarıyla eklendi!", text_color="green")
            ders_adi_entry.delete(0, 'end')
            ders_saati_entry.delete(0, 'end')
        else:
            mesaj = ctk.CTkLabel(root_frame, text="Lütfen tüm alanları doldurun!", text_color="red")

        mesaj.grid(row=4, column=0, columnspan=2, pady=10)

    kaydet_button = ctk.CTkButton(root_frame, text="Kaydet", command=kaydet)
    kaydet_button.grid(row=3, column=0, columnspan=2, pady=20)

    # Grid kolonlarını eşitle
    root_frame.grid_columnconfigure(0, weight=1)
    root_frame.grid_columnconfigure(1, weight=1)
