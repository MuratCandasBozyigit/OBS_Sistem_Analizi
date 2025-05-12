import customtkinter as ctk
from tkinter import messagebox
from DB.Migrations.Class import tum_dersleri_getir, ders_sil, ders_guncelle
from . import createClass

def dersleri_listele_gui():
    win = ctk.CTkToplevel()
    win.title("Ders Yönetimi")
    win.geometry("800x550")

    title = ctk.CTkLabel(win, text="Tüm Dersler", font=("Arial", 22, "bold"))
    title.pack(pady=10)

    ekle_btn = ctk.CTkButton(win, text="Yeni Ders Ekle",
                             command=createClass.ders_ekleme_penceresi,
                             fg_color="green", hover_color="#006400", font=("Arial", 14))
    ekle_btn.pack(pady=(0, 10))

    scroll_frame = ctk.CTkScrollableFrame(win, width=750, height=400)
    scroll_frame.pack(padx=20, pady=10, fill="both", expand=True)

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
        confirm = messagebox.askyesno("🚨 DERSİ SİLME ONAYI", f"⚠️ ID: {ders_id} olan dersi kalıcı olarak silmek üzeresiniz!\n\nBu işlem geri alınamaz. Emin misiniz?")
        if confirm:
            try:
                ders_sil(ders_id)
                frame.destroy()
                messagebox.showinfo("Silindi", f"Ders başarıyla silindi.")
            except Exception as e:
                messagebox.showerror("Hata", f"Ders silinirken bir hata oluştu: {e}")

    def guncelle_ders(ders_id, eski_ad, eski_saat):
        popup = ctk.CTkToplevel()
        popup.title("Dersi Güncelle")
        popup.geometry("300x200")

        ctk.CTkLabel(popup, text="Yeni Ders Adı:", font=("Arial", 14)).pack(pady=(10, 5))
        yeni_ad_entry = ctk.CTkEntry(popup)
        yeni_ad_entry.insert(0, eski_ad)
        yeni_ad_entry.pack(pady=5)

        ctk.CTkLabel(popup, text="Yeni Saat:", font=("Arial", 14)).pack(pady=(10, 5))
        yeni_saat_entry = ctk.CTkEntry(popup)
        yeni_saat_entry.insert(0, eski_saat)
        yeni_saat_entry.pack(pady=5)

        def kaydet():
            yeni_ad = yeni_ad_entry.get()
            yeni_saat = yeni_saat_entry.get()

            if not yeni_ad or not yeni_saat:
                messagebox.showwarning("Eksik Bilgi", "Lütfen tüm alanları doldurun.")
                return

            try:
                ders_guncelle(ders_id, yeni_ad, yeni_saat)
                messagebox.showinfo("Güncellendi", "Ders başarıyla güncellendi.")
                popup.destroy()
                win.destroy()
                dersleri_listele_gui()  # Sayfayı yenile
            except Exception as e:
                messagebox.showerror("Hata", f"Güncelleme sırasında hata oluştu: {e}")

        ctk.CTkButton(popup, text="Kaydet", command=kaydet, fg_color="blue").pack(pady=15)

    for i, ders in enumerate(dersler, start=1):
        ders_id, ders_adi, ders_saati = ders

        row_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent")
        row_frame.grid(row=i, column=0, columnspan=5, sticky="ew", pady=2)
        row_frame.bind("<Button-1>", lambda e, f=row_frame: satir_sec(e, f))

        label_id = ctk.CTkLabel(row_frame, text=str(ders_id), font=("Arial", 15), width=100, anchor="w")
        label_adi = ctk.CTkLabel(row_frame, text=ders_adi, font=("Arial", 15), width=200, anchor="w")
        label_saat = ctk.CTkLabel(row_frame, text=ders_saati, font=("Arial", 15), width=100, anchor="w")

        # Sil Butonu
        sil_btn = ctk.CTkButton(row_frame, text="Sil", fg_color="red", hover_color="#8B0000",
                                width=60, height=28, font=("Arial", 12),
                                command=lambda d_id=ders_id, f=row_frame: sil_ders(d_id, f))
        # Güncelle Butonu
        guncelle_btn = ctk.CTkButton(row_frame, text="Güncelle", fg_color="orange", hover_color="#CC8400",
                                     width=80, height=28, font=("Arial", 12),
                                     command=lambda d_id=ders_id, ad=ders_adi, saat=ders_saati: guncelle_ders(d_id, ad, saat))

        # Grid yerleşimi
        label_id.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        label_adi.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        label_saat.grid(row=0, column=2, padx=10, pady=5, sticky="w")
        sil_btn.grid(row=0, column=3, padx=(5, 5), pady=5)
        guncelle_btn.grid(row=0, column=4, padx=(5, 10), pady=5)

        # Satır seçimi
        for widget in [label_id, label_adi, label_saat]:
            widget.bind("<Button-1>", lambda e, f=row_frame: satir_sec(e, f))
