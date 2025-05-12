import customtkinter as ctk
from DB.Migrations.Class.read import tum_dersleri_getir

def dersleri_listele_gui():
    win = ctk.CTkToplevel()
    win.title("Ders Yönetimi")
    win.geometry("700x500")

    title = ctk.CTkLabel(win, text="Tüm Dersler", font=("Arial", 22, "bold"))
    title.pack(pady=10)

    # Ekleme Butonu
    ekle_btn = ctk.CTkButton(win, text="Yeni Ders Ekle", fg_color="green", hover_color="#006400", font=("Arial", 14))
    ekle_btn.pack(pady=(0, 10))

    scroll_frame = ctk.CTkScrollableFrame(win, width=650, height=350)
    scroll_frame.pack(padx=20, pady=10, fill="both", expand=True)

    # Kolon başlıkları
    headers = ["Ders ID", "Ders Adı", "Saat", "İşlemler"]
    for col, header in enumerate(headers):
        ctk.CTkLabel(scroll_frame, text=header, font=("Arial", 16, "bold")).grid(row=0, column=col, padx=10, pady=5, sticky="w")

    dersler = tum_dersleri_getir()
    if not dersler:
        ctk.CTkLabel(scroll_frame, text="Kayıtlı ders bulunamadı.", font=("Arial", 14)).grid(row=1, column=0, columnspan=4, pady=10)
        return

    selected = {"frame": None}

    def satir_sec(event, frame):
        if selected["frame"]:
            selected["frame"].configure(fg_color="transparent")
        frame.configure(fg_color="#D3D3D3")
        selected["frame"] = frame

    def sil_ders(ders_id):
        print(f"Silinecek ders ID: {ders_id}")
        # Veritabanından silme işlemini burada yap

    def guncelle_ders(ders_id):
        print(f"Güncellenecek ders ID: {ders_id}")
        # Güncelleme penceresini aç veya formu getir

    for i, ders in enumerate(dersler, start=1):
        ders_id, ders_adi, ders_saati = ders

        row_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent")
        row_frame.grid(row=i, column=0, columnspan=4, sticky="ew")
        row_frame.bind("<Button-1>", lambda e, f=row_frame: satir_sec(e, f))

        # Hücreler
        label_id = ctk.CTkLabel(row_frame, text=str(ders_id), font=("Arial", 15), width=100, anchor="w")
        label_adi = ctk.CTkLabel(row_frame, text=ders_adi, font=("Arial", 15), width=200, anchor="w")
        label_saat = ctk.CTkLabel(row_frame, text=ders_saati, font=("Arial", 15), width=100, anchor="w")

        # Butonlar
        guncelle_btn = ctk.CTkButton(row_frame, text="Güncelle", fg_color="#FFA500", hover_color="#cc8400",
                                     width=80, height=28, font=("Arial", 12),
                                     command=lambda d_id=ders_id: guncelle_ders(d_id))
        sil_btn = ctk.CTkButton(row_frame, text="Sil", fg_color="red", hover_color="#8B0000",
                                width=60, height=28, font=("Arial", 12),
                                command=lambda d_id=ders_id: sil_ders(d_id))

        # Grid yerleşimi
        label_id.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        label_adi.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        label_saat.grid(row=0, column=2, padx=10, pady=5, sticky="w")
        guncelle_btn.grid(row=0, column=3, padx=(10, 5), pady=5)
        sil_btn.grid(row=0, column=4, padx=(5, 10), pady=5)

        for widget in [label_id, label_adi, label_saat]:
            widget.bind("<Button-1>", lambda e, f=row_frame: satir_sec(e, f))
