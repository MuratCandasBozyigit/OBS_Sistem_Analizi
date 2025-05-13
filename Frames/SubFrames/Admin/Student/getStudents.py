import customtkinter as ctk
from tkinter import messagebox
from DB.Migrations.Student import tum_ogrencileri_getir, ogrenci_sil, ogrenci_guncelle
from . import createStudent

def ogrencileri_listele_gui():
    win = ctk.CTkToplevel()
    win.title("Öğrenci Yönetimi")
    win.geometry("1100x700")

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

    scroll_frame = ctk.CTkScrollableFrame(win, width=1100, height=460)
    scroll_frame.pack(padx=20, pady=10, fill="both", expand=True)

    headers = ["ID", "Adı", "Soyadı", "Telefon", "TCKN", "Numara", "Fotoğraf", "Adres", "Şifre", "İşlemler"]
    for col, header in enumerate(headers):
        ctk.CTkLabel(scroll_frame, text=header, font=("Arial", 15, "bold")).grid(
            row=0, column=col, padx=15, pady=5, sticky="w"
        )

    ogrenciler = tum_ogrencileri_getir()
    if not ogrenciler:
        ctk.CTkLabel(scroll_frame, text="Kayıtlı öğrenci bulunamadı.", font=("Arial", 25,"bold")).grid(
            row=3, column=5, columnspan=10, pady=10
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

    def guncelle_goster(row_idx, ogrenci_id, mevcut_ad, mevcut_soyad, mevcut_tel, mevcut_tckn, mevcut_numara, mevcut_foto, mevcut_adres, mevcut_sifre):
        if guncelle_form["frame"]:
            guncelle_form["frame"].destroy()

        form = ctk.CTkFrame(scroll_frame, fg_color="#F0F0F0")
        form.grid(row=row_idx+1, column=0, columnspan=10, pady=(5, 15), sticky="ew", padx=10)

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

        ctk.CTkLabel(form, text="Numara:", font=("Arial", 13)).grid(row=2, column=1, padx=5, pady=5, sticky="w")
        entry_numara = ctk.CTkEntry(form, width=200)
        entry_numara.insert(0, mevcut_numara)
        entry_numara.grid(row=2, column=2, padx=5, pady=5)

        ctk.CTkLabel(form, text="Fotoğraf URL:", font=("Arial", 13)).grid(row=2, column=3, padx=5, pady=5, sticky="w")
        entry_foto = ctk.CTkEntry(form, width=200)
        entry_foto.insert(0, mevcut_foto)
        entry_foto.grid(row=2, column=4, padx=5, pady=5)

        ctk.CTkLabel(form, text="Adres:", font=("Arial", 13)).grid(row=3, column=1, padx=5, pady=5, sticky="w")
        entry_adres = ctk.CTkEntry(form, width=200)
        entry_adres.insert(0, mevcut_adres)
        entry_adres.grid(row=3, column=2, padx=5, pady=5)

        ctk.CTkLabel(form, text="Şifre:", font=("Arial", 13)).grid(row=3, column=3, padx=5, pady=5, sticky="w")
        entry_sifre = ctk.CTkEntry(form, width=200, show="*")
        entry_sifre.insert(0, mevcut_sifre)
        entry_sifre.grid(row=3, column=4, padx=5, pady=5)

        def kaydet():
            yeni_ad = entry_ad.get().strip()
            yeni_soyad = entry_soyad.get().strip()
            yeni_tel = entry_tel.get().strip()
            yeni_tckn = entry_tckn.get().strip()
            yeni_numara = entry_numara.get().strip()
            yeni_foto = entry_foto.get().strip()
            yeni_adres = entry_adres.get().strip()
            yeni_sifre = entry_sifre.get().strip()

            if not yeni_ad or not yeni_soyad or not yeni_tel or not yeni_tckn or not yeni_numara or not yeni_foto or not yeni_adres or not yeni_sifre:
                messagebox.showerror("Hata", "Alanlar boş bırakılamaz.")
                return

            try:
                ogrenci_guncelle(ogrenci_id, yeni_ad, yeni_soyad, yeni_foto, yeni_adres, yeni_tel, yeni_tckn, yeni_numara, yeni_sifre)
                messagebox.showinfo("Başarılı", "Öğrenci güncellendi.")
                win.destroy()
                ogrencileri_listele_gui()
            except Exception as e:
                messagebox.showerror("Hata", f"Güncelleme hatası:\n{e}")

        guncelle_btn = ctk.CTkButton(form, text="Kaydet", command=kaydet, width=100, fg_color="#FFA500", hover_color="#FF8C00")
        guncelle_btn.grid(row=4, column=4, padx=10)
        iptal_btn = ctk.CTkButton(form, text="İptal", command=iptal_et, width=80, fg_color="gray", hover_color="darkgray")
        iptal_btn.grid(row=4, column=5, padx=(0, 10), pady=5)

        guncelle_form["frame"] = form

    for i, ogrenci in enumerate(ogrenciler, start=1):
        ogrenci_id, ogrenci_adı, ogrenci_soyadı, ogrenci_fotoğraf, ogrenci_adres, ogrenci_tel_no, ogrenci_tckn, ogrenci_numarası, sifre = ogrenci

        row_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent")
        row_frame.grid(row=i, column=0, columnspan=10, sticky="ew", pady=2, padx=5)

        label_id = ctk.CTkLabel(row_frame, text=str(ogrenci_id), font=("Arial", 12))
        label_id.grid(row=0, column=0, padx=5, pady=5)

        label_ad = ctk.CTkLabel(row_frame, text=ogrenci_adı, font=("Arial", 12))
        label_ad.grid(row=0, column=1, padx=5, pady=5)

        label_soyad = ctk.CTkLabel(row_frame, text=ogrenci_soyadı, font=("Arial", 12))
        label_soyad.grid(row=0, column=2, padx=5, pady=5)

        label_tel = ctk.CTkLabel(row_frame, text=ogrenci_tel_no, font=("Arial", 12))
        label_tel.grid(row=0, column=3, padx=5, pady=5)

        label_tckn = ctk.CTkLabel(row_frame, text=ogrenci_tckn, font=("Arial", 12))
        label_tckn.grid(row=0, column=4, padx=5, pady=5)

        label_numara = ctk.CTkLabel(row_frame, text=ogrenci_numarası, font=("Arial", 12))
        label_numara.grid(row=0, column=5, padx=5, pady=5)

        label_foto = ctk.CTkLabel(row_frame, text=ogrenci_fotoğraf, font=("Arial", 12))
        label_foto.grid(row=0, column=6, padx=5, pady=5)

        label_adres = ctk.CTkLabel(row_frame, text=ogrenci_adres, font=("Arial", 12))
        label_adres.grid(row=0, column=7, padx=5, pady=5)

        label_sifre = ctk.CTkLabel(row_frame, text=ogrenci_adres, font=("Arial", 12))
        label_sifre.grid(row=0, column=8, padx=5, pady=5)

        guncelle_btn = ctk.CTkButton(
            row_frame, text="Güncelle", font=("Arial", 12), fg_color="#FFA500", hover_color="#FF8C00", 
            command=lambda row=i, ogrenci_id=ogrenci_id, ad=ogrenci_adı, soyad=ogrenci_soyadı, tel=ogrenci_tel_no, tckn=ogrenci_tckn, numara=ogrenci_numarası, foto=ogrenci_fotoğraf, adres=ogrenci_adres, sifre=sifre: guncelle_goster(row, ogrenci_id, ad, soyad, tel, tckn, numara, foto, adres, sifre)
        )
        guncelle_btn.grid(row=0, column=9, padx=5, pady=5)

        sil_btn = ctk.CTkButton(
            row_frame, text="Sil", font=("Arial", 12), fg_color="#FF6347", hover_color="#FF4500", 
            command=lambda ogrenci_id=ogrenci_id, row_frame=row_frame: sil_ogrenci(ogrenci_id, row_frame)
        )
        sil_btn.grid(row=0, column=10, padx=5, pady=5)
