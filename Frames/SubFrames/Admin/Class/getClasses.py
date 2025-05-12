import customtkinter as ctk
from tkinter import messagebox
from DB.Migrations.Class import tum_dersleri_getir, ders_sil, ders_guncelle
from . import createClass


def dersleri_listele_gui():
    win = ctk.CTkToplevel()
    win.title("Ders Yönetimi")
    win.geometry("750x600")

    title = ctk.CTkLabel(win, text="Tüm Dersler", font=("Arial", 22, "bold"))
    title.pack(pady=10)

    ekle_btn = ctk.CTkButton(win, text="Yeni Ders Ekle",
                             command=createClass.ders_ekleme_penceresi,
                             fg_color="green", hover_color="#006400", font=("Arial", 14))
    ekle_btn.pack(pady=(0, 10))

    scroll_frame = ctk.CTkScrollableFrame(win, width=700, height=460)
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

    def sil_ders(ders_id, frame):
        confirm = messagebox.askyesno("Dersi Sil", f"ID: {ders_id} olan dersi silmek istiyor musun?")
        if confirm:
            try:
                ders_sil(ders_id)
                frame.destroy()
                messagebox.showinfo("Silindi", "Ders başarıyla silindi.")
            except Exception as e:
                messagebox.showerror("Hata", f"Silinemedi!\n{e}")

    # Güncelleme formunu oluşturmak için geçici tutucu
    guncelle_form = {"frame": None}

    def guncelle_goster(row_idx, ders_id, mevcut_ad, mevcut_saat):
        if guncelle_form["frame"]:
            guncelle_form["frame"].destroy()

        form = ctk.CTkFrame(scroll_frame, fg_color="#F0F0F0")
        form.grid(row=row_idx+1, column=0, columnspan=5, pady=(5, 15), sticky="ew", padx=10)

        ctk.CTkLabel(form, text="Ders Adı:", font=("Arial", 13)).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        entry_ad = ctk.CTkEntry(form, width=200)
        entry_ad.insert(0, mevcut_ad)
        entry_ad.grid(row=0, column=1, padx=5, pady=5)

        ctk.CTkLabel(form, text="Ders Saati:", font=("Arial", 13)).grid(row=0, column=2, padx=5, pady=5, sticky="w")
        entry_saat = ctk.CTkEntry(form, width=100)
        entry_saat.insert(0, mevcut_saat)
        entry_saat.grid(row=0, column=3, padx=5, pady=5)

        def kaydet():
            yeni_ad = entry_ad.get().strip()
            yeni_saat = entry_saat.get().strip()

            if not yeni_ad or not yeni_saat:
                messagebox.showerror("Hata", "Alanlar boş bırakılamaz.")
                return

            try:
                ders_guncelle(ders_id, yeni_ad, yeni_saat)
                messagebox.showinfo("Başarılı", "Ders güncellendi.")
                win.destroy()
                dersleri_listele_gui()
            except Exception as e:
                messagebox.showerror("Hata", f"Güncelleme hatası:\n{e}")

        guncelle_btn = ctk.CTkButton(form, text="Kaydet", command=kaydet, width=100)
        guncelle_btn.grid(row=0, column=4, padx=10)

        guncelle_form["frame"] = form

    for i, ders in enumerate(dersler, start=1):
        ders_id, ders_adi, ders_saati = ders

        row_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent")
        row_frame.grid(row=i, column=0, columnspan=5, sticky="ew", pady=2, padx=5)

        label_id = ctk.CTkLabel(row_frame, text=str(ders_id), font=("Arial", 15), width=80, anchor="w")
        label_adi = ctk.CTkLabel(row_frame, text=ders_adi, font=("Arial", 15), width=200, anchor="w")
        label_saat = ctk.CTkLabel(row_frame, text=ders_saati, font=("Arial", 15), width=100, anchor="w")

        sil_btn = ctk.CTkButton(row_frame, text="Sil", fg_color="red", hover_color="#8B0000",
                                width=60, height=28, font=("Arial", 12),
                                command=lambda d_id=ders_id, f=row_frame: sil_ders(d_id, f))

        guncelle_btn = ctk.CTkButton(row_frame, text="Güncelle", fg_color="#FFA500", hover_color="#cc8400",
                                     width=80, height=28, font=("Arial", 12),
                                     command=lambda idx=i, d_id=ders_id, d_adi=ders_adi, d_saat=ders_saati:
                                     guncelle_goster(idx, d_id, d_adi, d_saat))

        label_id.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        label_adi.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        label_saat.grid(row=0, column=2, padx=10, pady=5, sticky="w")
        sil_btn.grid(row=0, column=3, padx=(5, 5), pady=5)
        guncelle_btn.grid(row=0, column=4, padx=(5, 10), pady=5)
