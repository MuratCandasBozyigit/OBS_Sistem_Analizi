import customtkinter as ctk
from tkinter import messagebox
from DB.Migrations.Class import tum_dersleri_getir, ders_sil
from . import createClass

def dersleri_listele_gui():
    win = ctk.CTkToplevel()
    win.title("Ders Yönetimi")
    win.geometry("700x500")

    title = ctk.CTkLabel(win, text="Tüm Dersler", font=("Arial", 22, "bold"))
    title.pack(pady=10)

    # Ekleme Butonu
    ekle_btn = ctk.CTkButton(win, text="Yeni Ders Ekle",
                             command=createClass.ders_ekleme_penceresi,
                             fg_color="green", hover_color="#006400", font=("Arial", 14))
    ekle_btn.pack(pady=(0, 10))

    scroll_frame = ctk.CTkScrollableFrame(win, width=650, height=350)
    scroll_frame.pack(padx=20, pady=10, fill="both", expand=True)

    # Kolon başlıkları
    headers = ["Ders ID", "Ders Adı", "Saat", "İşlemler"]
    for col, header in enumerate(headers):
        ctk.CTkLabel(scroll_frame, text=header, font=("Arial", 16, "bold")).grid(
            row=0, column=col, padx=10, pady=5, sticky="w"
        )

    dersler = tum_dersleri_getir()
    if not dersler:
        ctk.CTkLabel(scroll_frame, text="Kayıtlı ders bulunamadı.", font=("Arial", 14)).grid(
            row=1, column=0, columnspan=4, pady=10
        )
        return

    selected = {"frame": None}

    def satir_sec(event, frame):
        if selected["frame"]:
            selected["frame"].configure(fg_color="transparent")
        frame.configure(fg_color="#D3D3D3")
        selected["frame"] = frame

    def sil_ders(ders_id, frame):
        confirm = messagebox.askyesno("Dersi Sil", f"ID: {ders_id} olan dersi silmek istediğinize emin misiniz?")
        if confirm:
            ders_sil(ders_id)  # DB'den sil
            frame.destroy()    # GUI'den kaldır

    for i, ders in enumerate(dersler, start=1):
        ders_id, ders_adi, ders_saati = ders

        row_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent")
        row_frame.grid(row=i, column=0, columnspan=5, sticky="ew")
        row_frame.bind("<Button-1>", lambda e, f=row_frame: satir_sec(e, f))

        # Hücreler
        label_id = ctk.CTkLabel(row_frame, text=str(ders_id), font=("Arial", 15), width=100, anchor="w")
        label_adi = ctk.CTkLabel(row_frame, text=ders_adi, font=("Arial", 15), width=200, anchor="w")
        label_saat = ctk.CTkLabel(row_frame, text=ders_saati, font=("Arial", 15), width=100, anchor="w")

        # Sil Butonu
        sil_btn = ctk.CTkButton(row_frame, text="Sil", fg_color="red", hover_color="#8B0000",
                                width=60, height=28, font=("Arial", 12),
                                command=lambda d_id=ders_id, f=row_frame: sil_ders(d_id, f))

        # Grid yerleşimi
        label_id.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        label_adi.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        label_saat.grid(row=0, column=2, padx=10, pady=5, sticky="w")
        sil_btn.grid(row=0, column=3, padx=(5, 10), pady=5)

        # Satır seçimi için tüm label'lara bind
        for widget in [label_id, label_adi, label_saat]:
            widget.bind("<Button-1>", lambda e, f=row_frame: satir_sec(e, f))
