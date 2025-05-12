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

    title_label = ctk.CTkLabel(root_frame, text="Yeni Ders Ekle", font=("Arial", 18))
    title_label.grid(row=0, column=0, columnspan=2, pady=20)

    ders_adi_label = ctk.CTkLabel(root_frame, text="Ders Adı:")
    ders_adi_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    ders_adi_entry = ctk.CTkEntry(root_frame)
    ders_adi_entry.grid(row=1, column=1, padx=10, pady=10)

    ders_saati_label = ctk.CTkLabel(root_frame, text="Ders Saati:")
    ders_saati_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

    ders_saati_entry = ctk.CTkEntry(root_frame)
    ders_saati_entry.grid(row=2, column=1, padx=10, pady=10)

    def kaydet():
        ders_adi = ders_adi_entry.get()
        ders_saati = ders_saati_entry.get()

        for widget in root_frame.grid_slaves(row=4):  # Önceki mesajları temizle
            widget.destroy()

        if ders_adi and ders_saati:
            ders_ekle(ders_adi, ders_saati)
            ctk.CTkLabel(root_frame, text="Ders başarıyla eklendi!", text_color="green").grid(row=4, column=0, columnspan=2, pady=10)
            ders_adi_entry.delete(0, 'end')
            ders_saati_entry.delete(0, 'end')
        else:
            ctk.CTkLabel(root_frame, text="Lütfen tüm alanları doldurun!", text_color="red").grid(row=4, column=0, columnspan=2, pady=10)

    kaydet_button = ctk.CTkButton(root_frame, text="Kaydet", command=kaydet)
    kaydet_button.grid(row=3, column=0, columnspan=2, pady=20)
