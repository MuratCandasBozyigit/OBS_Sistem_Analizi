import customtkinter as ctk

# CustomTkinter tema ayarları
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Dersleri Göster Sayfası
def dersleri_goster():
    print("Tüm Dersler Gösteriliyor...")

# Ders Ekle Sayfası
def ders_ekle():
    print("Yeni Ders Ekleme Sayfası Açılıyor...")

# Ders Sil Sayfası
def ders_sil():
    print("Ders Silme Sayfası Açılıyor...")

# Ders Güncelle Sayfası
def ders_guncelle():
    print("Ders Güncelleme Sayfası Açılıyor...")

# Ana Yönetim Sayfası
def dersler_yonetim_penceresi():
    win = ctk.CTkToplevel()
    win.title("Ders Yönetimi")
    win.geometry("500x400")

    # CTkFrame ile arayüz konteyneri
    frame = ctk.CTkFrame(win)
    frame.pack(expand=True, fill="both", padx=20, pady=20)

    # Başlık
    title_label = ctk.CTkLabel(frame, text="Ders Yönetimi", font=("Arial", 24, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=(10, 30))

    # Butonlar
    show_all_button = ctk.CTkButton(frame, text="Tüm Dersleri Göster", command=dersleri_goster)
    show_all_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    add_class_button = ctk.CTkButton(frame, text="Ders Ekle", command=ders_ekle)
    add_class_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    delete_class_button = ctk.CTkButton(frame, text="Ders Sil", command=ders_sil)
    delete_class_button.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    update_class_button = ctk.CTkButton(frame, text="Ders Güncelle", command=ders_guncelle)
    update_class_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    # Grid düzeni
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)

# Ana pencereyi test için çalıştır
if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Ana Menü")
    app.geometry("400x300")

    open_button = ctk.CTkButton(app, text="Ders Yönetim Panelini Aç", command=dersler_yonetim_penceresi)
    open_button.pack(pady=100)

    app.mainloop()
