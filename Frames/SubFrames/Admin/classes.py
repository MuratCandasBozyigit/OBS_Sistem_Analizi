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
    # Tüm önceki widget'ları temizle
    for widget in root_frame.winfo_children():
        widget.destroy()

    # Başlık
    title_label = ctk.CTkLabel(root_frame, text="Ders Yönetimi", font=("Arial", 24, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=30)

    # Butonlar
    buttons = [
        ("Tüm Dersleri Göster", dersleri_goster),
        ("Ders Ekle", ders_ekle),
        ("Ders Sil", ders_sil),
        ("Ders Güncelle", ders_guncelle)
    ]

    for idx, (text, command) in enumerate(buttons):
        button = ctk.CTkButton(root_frame, text=text, width=200, height=50, command=command, fg_color="blue", hover_color="darkblue")
        button.grid(row=idx + 1, column=0, pady=10, padx=10, ipadx=10, ipady=10, sticky="ew")

    # Tasarım Özellikleri
    root_frame.grid_rowconfigure(0, weight=1)
    root_frame.grid_rowconfigure(1, weight=1)
    root_frame.grid_columnconfigure(0, weight=1)

    # Butonlar arası mesafe ve kenar boşlukları
    for button in [button for _, button in buttons]:
        button.grid_configure(padx=20, pady=10)

    # Butonları ortalamak
    root_frame.grid_columnconfigure(0, weight=1)

    # Görsel olarak hoş bir görünüm için stil ekledik
    for button in [button for _, button in buttons]:
        button.configure(fg_color="blue", hover_color="darkblue", font=("Arial", 14, "bold"))
        
    # Arka plan rengi
    root_frame.configure(bg="#f5f5f5")

# Eğer program çalıştırılacaksa aşağıdaki kodu aktif edin
# dersler_yonetim_penceresi()
