import customtkinter as ctk

# Dersleri Göster Sayfası
def dersleri_goster():
    print("Tüm Dersler Gösteriliyor...")  # Burada dersleri listeleyeceksiniz.

# Ders Ekle Sayfası
def ders_ekle():
    print("Yeni Ders Ekleme Sayfası Açılıyor...")  # Burada yeni ders ekleme sayfasını açabilirsiniz.

# Ders Sil Sayfası
def ders_sil():
    print("Ders Silme Sayfası Açılıyor...")  # Burada ders silme işlemi yapılabilir.

# Ders Güncelle Sayfası
def ders_guncelle():
    print("Ders Güncelleme Sayfası Açılıyor...")  # Burada ders güncelleme işlemi yapılabilir.

# Ana Yönetim Sayfası
def dersler_yonetim_penceresi():
    win = ctk.CTkToplevel()
    win.title("Ders Yönetimi")
    win.geometry("500x400")
    dersler_yonetim_sayfasi(win)

def dersler_yonetim_sayfasi(root_frame):
    for widget in root_frame.winfo_children():
        widget.destroy()

    title_label = ctk.CTkLabel(root_frame, text="Ders Yönetimi", font=("Arial", 18))
    title_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Tüm Dersleri Göster Butonu
    show_all_button = ctk.CTkButton(root_frame, text="Tüm Dersleri Göster", command=dersleri_goster)
    show_all_button.grid(row=1, column=0, pady=10, padx=10)

    # Ders Ekle Butonu
    add_class_button = ctk.CTkButton(root_frame, text="Ders Ekle", command=ders_ekle)
    add_class_button.grid(row=2, column=0, pady=10, padx=10)

    # Ders Sil Butonu
    delete_class_button = ctk.CTkButton(root_frame, text="Ders Sil", command=ders_sil)
    delete_class_button.grid(row=3, column=0, pady=10, padx=10)

    # Ders Güncelle Butonu
    update_class_button = ctk.CTkButton(root_frame, text="Ders Güncelle", command=ders_guncelle)
    update_class_button.grid(row=4, column=0, pady=10, padx=10)

    # # Geri Butonu
    # back_button = ctk.CTkButton(root_frame, text="Ana Sayfaya Dön", command=root_frame.destroy)
    # back_button.grid(row=5, column=0, pady=10, padx=10)

    

