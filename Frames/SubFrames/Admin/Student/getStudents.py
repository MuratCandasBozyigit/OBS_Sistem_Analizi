import customtkinter as ctk
from tkinter import messagebox
from DB.Migrations.Student import tum_ogrencileri_getir, ogrenci_sil, ogrenci_guncelle
from . import createStudent

def ogrencileri_listele_gui():
    win = ctk.CTkToplevel()
    win.title("Öğrenci Yönetimi")
    win.geometry("900x700")

    title = ctk.CTkLabel(win, text="Tüm Öğrenciler", font=("Arial", 22, "bold"))
    title.pack(pady=10)

    def refresh():
        win.destroy()
        ogrencileri_listele_gui()

    button_frame = ctk.CTkFrame(win, fg_color="transparent")
    button_frame.pack(pady=(0, 10))

    yenile_btn = ctk.CTkButton(
        button_frame,
        text="Sayfayı Yenile 🔁",
        command=refresh,
        fg_color="gray", hover_color="darkgray", font=("Arial", 14)
    )
    yenile_btn.pack(side="left", padx=10)

    ekle_btn = ctk.CTkButton(
        button_frame,
        text="Yeni Öğrenci Ekle",
        command=createStudent.ogrenci_ekleme_penceresi,
        fg_color="green", hover_color="#006400", font=("Arial", 14)
    )
    ekle_btn.pack(side="left", padx=10)

    scroll_frame = ctk.CTkScrollableFrame(win, width=900, height=460)
    scroll_frame.pack(padx=20, pady=10, fill="both", expand=True)

    headers = ["Öğrenci ID", "Adı", "Soyadı", "Telefon", "TCKN", "İşlemler"]
    for col, header in enumerate(headers):
        ctk.CTkLabel(scroll_frame, text=header, font=("Arial", 16, "bold")).grid(
            row=0, column=col, padx=10, pady=5, sticky="w"
        )

    ogrenciler = tum_ogrencileri_getir()  # Bu fonksiyon tüm öğrencileri alır
    if not ogrenciler:
        ctk.CTkLabel(scroll_frame, text="Kayıtlı öğrenci bulunamadı.", font=("Arial", 14)).grid(
            row=1, column=0, columnspan=6, pady=10
        )
        return

    def sil_ogrenci(ogrenci_id, frame):
        confirm = messagebox.askyesno("Öğrenciyi Sil", f"ID: {ogrenci_id} olan öğrenciyi silmek istiyor musunuz?")
        if confirm:
            try:
                ogrenci_sil(ogrenci_id)
                frame.destroy()
                messagebox.showinfo("Silindi", "Öğrenci başarıyla silindi.")
            except Exception as e:
                messagebox.showerror("Hata", f"Silinemedi!\n{e}")

    guncelle_form = {"frame": None}

    def guncelle_goster(row_idx, ogrenci_id, mevcut_ad, mevcut_soyad, mevcut_tel, mevcut_tckn):
        if guncelle_form["frame"]:
            guncelle_form["frame"].destroy()

        form = ctk.CTkFrame(scroll_frame, fg_color="#F0F0F0")
        form.grid(row=row_idx+1, column=0, columnspan=6, pady=(5, 15), sticky="ew", padx=10)

        def iptal_et():
            form.destroy()
            guncelle_form["frame"] = None

        ctk.CTkLabel(form, text="Adı:", font=("Arial", 13)).grid(row=0, column=1, padx=5, pady=5, sticky="w")
        entry_ad = ctk.CTkEntry(form, width=200)
        entry_ad.insert(0, mevcut_ad)
        entry_ad.grid(row=0, column=2, padx=5, pady=5)

        ctk.CTkLabel(form, text="Soyadı:", font=("Arial", 13)).grid(row=0, column=3, padx=5, pady=5, sticky="w")
        entry_soyad = ctk.CTkEntry(form, width=200)
        entry_soyad.insert(0, mevcut_soyad)
        entry_soyad.grid(row=0, column=4, padx=5, pady=5)

        ctk.CTkLabel(form, text="Telefon No:", font=("Arial", 13)).grid(row=1, column=1, padx=5, pady=5, sticky="w")
        entry_tel = ctk.CTkEntry(form, width=200)
        entry_tel.insert(0, mevcut_tel)
        entry_tel.grid(row=1, column=2, padx=5, pady=5)

        ctk.CTkLabel(form, text="TCKN:", font=("Arial", 13)).grid(row=1, column=3, padx=5, pady=5, sticky="w")
        entry_tckn = ctk.CTkEntry(form, width=200)
        entry_tckn.insert(0, mevcut_tckn)
        entry_tckn.grid(row=1, column=4, padx=5, pady=5)

        def kaydet():
            yeni_ad = entry_ad.get().strip()
            yeni_soyad = entry_soyad.get().strip()
            yeni_tel = entry_tel.get().strip()
            yeni_tckn = entry_tckn.get().strip()

            if not yeni_ad or not yeni_soyad or not yeni_tel or not yeni_tckn:
                messagebox.showerror("Hata", "Alanlar boş bırakılamaz.")
                return

            try:
                ogrenci_guncelle(ogrenci_id, yeni_ad, yeni_soyad, yeni_tel, yeni_tckn)
                messagebox.showinfo("Başarılı", "Öğrenci güncellendi.")
                win.destroy()
                ogrencileri_listele_gui()
            except Exception as e:
                messagebox.showerror("Hata", f"Güncelleme hatası:\n{e}")

        guncelle_btn = ctk.CTkButton(form, text="Kaydet", command=kaydet, width=100)
        guncelle_btn.grid(row=1, column=5, padx=10)
        iptal_btn = ctk.CTkButton(form, text="İptal", command=iptal_et, width=80, fg_color="gray", hover_color="darkgray")
        iptal_btn.grid(row=1, column=6, padx=(0, 10), pady=5)

        guncelle_form["frame"] = form

    for i, ogrenci in enumerate(ogrenciler, start=1):
        ogrenci_id, ogrenci_adi, ogrenci_soyadi, ogrenci_tel_no, ogrenci_tckn = ogrenci

        row_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent")
        row_frame.grid(row=i, column=0, columnspan=6, sticky="ew", pady=2, padx=5)

        label_id = ctk.CTkLabel(row_frame, text=str(ogrenci_id), font=("Arial", 15), width=80, anchor="w")
        label_adi = ctk.CTkLabel(row_frame, text=ogrenci_adi, font=("Arial", 15), width=200, anchor="w")
        label_soyadi = ctk.CTkLabel(row_frame, text=ogrenci_soyadi, font=("Arial", 15), width=200, anchor="w")
        label_tel = ctk.CTkLabel(row_frame, text=ogrenci_tel_no, font=("Arial", 15), width=150, anchor="w")
        label_tckn = ctk.CTkLabel(row_frame, text=ogrenci_tckn, font=("Arial", 15), width=150, anchor="w")

        sil_btn = ctk.CTkButton(row_frame, text="Sil", fg_color="red", hover_color="#8B0000",
                                width=60, height=28, font=("Arial", 12),
                                command=lambda o_id=ogrenci_id, f=row_frame: sil_ogrenci(o_id, f))

        guncelle_btn = ctk.CTkButton(row_frame, text="Güncelle", fg_color="#FFA500", hover_color="#cc8400",
                                     width=80, height=28, font=("Arial", 12),
                                     command=lambda idx=i, o_id=ogrenci_id, o_adi=ogrenci_adi, o_soyad=ogrenci_soyadi, 
                                              o_tel=ogrenci_tel_no, o_tckn=ogrenci_tckn: 
                                     guncelle_goster(idx, o_id, o_adi, o_soyad, o_tel, o_tckn))

        label_id.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        label_adi.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        label_soyadi.grid(row=0, column=2, padx=10, pady=5, sticky="w")
        label_tel.grid(row=0, column=3, padx=10, pady=5, sticky="w")
        label_tckn.grid(row=0, column=4, padx=10, pady=5, sticky="w")
        sil_btn.grid(row=0, column=5, padx=(5, 5), pady=5)
        guncelle_btn.grid(row=0, column=6, padx=(5, 10), pady=5)
