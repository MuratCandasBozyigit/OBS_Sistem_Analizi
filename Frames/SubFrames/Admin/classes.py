import customtkinter as ctk

# Tema ayarları
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
    win.geometry("600x300")  # pencere boyutu büyütüldü

    # Arayüz alanı
    frame = ctk.CTkFrame(win)
    frame.pack(expand=True, fill="both", padx=20, pady=20)

    # Başlık
    title_label = ctk.CTkLabel(frame, text="Ders Yönetimi", font=("Arial", 28, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=(10, 30))

    # %175 oranında büyütülmüş boyutlar
    button_width = int(180 * 1.3)    # ~315
    button_height = int(40 * 1.3)    # ~70
    button_font = ("Arial", int(14 * 1.3), "bold")  # ~24pt

    # Butonlar
    show_all_button = ctk.CTkButton(frame, text="Tüm Dersleri Göster", command=dersleri_goster,
                                    width=button_width, height=button_height, font=button_font)
    show_all_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    add_class_button = ctk.CTkButton(frame, text="Ders Ekle", command=ders_ekle,
                                     width=button_width, height=button_height, font=button_font)
    add_class_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    delete_class_button = ctk.CTkButton(frame, text="Ders Sil", command=ders_sil,
                                        width=button_width, height=button_height, font=button_font)
    delete_class_button.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    update_class_button = ctk.CTkButton(frame, text="Ders Güncelle", command=ders_guncelle,
                                        width=button_width, height=button_height, font=button_font)
    update_class_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    # Grid genişliği eşit olsun
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)

