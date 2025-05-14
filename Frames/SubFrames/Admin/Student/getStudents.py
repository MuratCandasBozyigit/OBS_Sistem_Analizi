import customtkinter as ctk
from tkinter import messagebox
from DB.Migrations.Student import tum_ogrencileri_getir, ogrenci_sil, ogrenci_guncelle
from . import createStudent  # Öğrenci ekleme penceresi
from . import assignClassToStudent

def ogrencileri_listele_gui():
    win = ctk.CTkToplevel()
    win.title("Öğrenci Yönetimi")
    win.geometry("1300x650")

    title = ctk.CTkLabel(win, text="Tüm Öğrenciler", font=("Arial", 22, "bold"))
    title.pack(pady=10)

    def refresh():
        win.destroy()
        ogrencileri_listele_gui()

    button_frame = ctk.CTkFrame(win, fg_color="transparent")
    button_frame.pack(pady=(0, 10))

    yenile_btn = ctk.CTkButton(
        button_frame, text="Sayfayı Yenile 🔁", command=refresh,
        fg_color="gray", hover_color="darkgray", font=("Arial", 14)
    )
    yenile_btn.pack(side="left", padx=10)

    ekle_btn = ctk.CTkButton(
        button_frame, text="Yeni Öğrenci Ekle",
        command=createStudent.ogrenci_ekleme_penceresi,
        fg_color="green", hover_color="#006400", font=("Arial", 14)
    )
    ekle_btn.pack(side="left", padx=10)

    scroll_frame = ctk.CTkScrollableFrame(win, width=1200, height=460)
    scroll_frame.pack(padx=20, pady=10, fill="both", expand=True)

    headers = ["ID", "Adı", "Soyadı", "Telefon", "TCKN", "Numara", "Fotoğraf", "Adres", "Şifre", "Güncelle", "Sil", "Ders İşlemleri","Öğretmen İşlemleri"]
    for col, header in enumerate(headers):
        ctk.CTkLabel(scroll_frame, text=header, font=("Arial", 15, "bold")).grid(
            row=0, column=col, padx=15, pady=5, sticky="w"
        )

    ogrenciler = tum_ogrencileri_getir()
    if not ogrenciler:
        ctk.CTkLabel(scroll_frame, text="Kayıtlı öğrenci bulunamadı.", font=("Arial", 25, "bold")).grid(
            row=3, column=5, columnspan=10, pady=10
        )
        return

    guncelle_form = {"frame": None}

    def sil_ogrenci(ogrenci_id):
        confirm = messagebox.askyesno("Öğrenciyi Sil", f"ID: {ogrenci_id} olan öğrenciyi silmek istiyor musunuz?")
        if confirm:
            try:
                ogrenci_sil(ogrenci_id)
                messagebox.showinfo("Silindi", "Öğrenci başarıyla silindi.")
                refresh()
            except Exception as e:
                messagebox.showerror("Hata", f"Silinemedi!\n{e}")

    def guncelle_goster(row_idx, ogrenci_id, mevcut_ad, mevcut_soyad, mevcut_tel, mevcut_tckn, mevcut_numara, mevcut_foto, mevcut_adres, mevcut_sifre):
        if guncelle_form["frame"]:
            guncelle_form["frame"].destroy()

        form = ctk.CTkFrame(scroll_frame, fg_color="#F0F0F0")
        form.grid(row=row_idx+1, column=0, columnspan=12, pady=(5, 15), sticky="ew", padx=10)

        def iptal_et():
            form.destroy()
            guncelle_form["frame"] = None

        def add_label_entry(row, col, text, mevcut, show=None):
            ctk.CTkLabel(form, text=text, font=("Arial", 13)).grid(row=row, column=col, padx=5, pady=5, sticky="w")
            entry = ctk.CTkEntry(form, width=200, show=show)
            entry.insert(0, mevcut)
            entry.grid(row=row, column=col+1, padx=5, pady=5)
            return entry

        entry_ad = add_label_entry(0, 1, "Adı:", mevcut_ad)
        entry_soyad = add_label_entry(0, 3, "Soyadı:", mevcut_soyad)
        entry_tel = add_label_entry(1, 1, "Telefon No:", mevcut_tel)
        entry_tckn = add_label_entry(1, 3, "TCKN:", mevcut_tckn)
        entry_numara = add_label_entry(2, 1, "Öğrenci No:", mevcut_numara)
        entry_foto = add_label_entry(2, 3, "Fotoğraf URL:", mevcut_foto)
        entry_adres = add_label_entry(3, 1, "Adres:", mevcut_adres)
        entry_sifre = add_label_entry(3, 3, "Şifre:", mevcut_sifre, show="*")

        def kaydet():
            yeni_ad = entry_ad.get().strip()
            yeni_soyad = entry_soyad.get().strip()
            yeni_tel = entry_tel.get().strip()
            yeni_tckn = entry_tckn.get().strip()
            yeni_numara = entry_numara.get().strip()
            yeni_foto = entry_foto.get().strip()
            yeni_adres = entry_adres.get().strip()
            yeni_sifre = entry_sifre.get().strip()

            if not all([yeni_ad, yeni_soyad, yeni_tel, yeni_tckn, yeni_numara, yeni_foto, yeni_adres, yeni_sifre]):
                messagebox.showerror("Hata", "Alanlar boş bırakılamaz.")
                return

            try:
                ogrenci_guncelle(ogrenci_id, yeni_ad, yeni_soyad, yeni_foto, yeni_adres, yeni_tel, yeni_tckn, yeni_numara, yeni_sifre)
                messagebox.showinfo("Başarılı", "Öğrenci güncellendi.")
                refresh()
            except Exception as e:
                messagebox.showerror("Hata", f"Güncelleme hatası:\n{e}")

        ctk.CTkButton(form, text="Kaydet", command=kaydet, width=100, fg_color="#FFA500", hover_color="#FF8C00").grid(row=4, column=4, padx=10)
        ctk.CTkButton(form, text="İptal", command=iptal_et, width=80, fg_color="gray", hover_color="darkgray").grid(row=4, column=5, padx=10, pady=5)

        guncelle_form["frame"] = form

    for i, ogrenci in enumerate(ogrenciler, start=1):
        ogrenci_id, ad, soyad, foto, adres, tel, tckn, numara, sifre = ogrenci

        for idx, val in enumerate([ogrenci_id, ad, soyad, tel, tckn, numara, foto, adres, sifre]):
            ctk.CTkLabel(scroll_frame, text=str(val), font=("Arial", 12)).grid(
                row=i, column=idx, padx=5, pady=5, sticky="w"
            )

        ctk.CTkButton(
            scroll_frame, text="Güncelle", font=("Arial", 12), fg_color="#FFA500", hover_color="#FF8C00",
            command=lambda row=i, oid=ogrenci_id: guncelle_goster(
                row, oid, ad, soyad, tel, tckn, numara, foto, adres, sifre
            )
        ).grid(row=i, column=9, padx=5, pady=5)

        ctk.CTkButton(
            scroll_frame, text="Sil", font=("Arial", 12), fg_color="#FF6347", hover_color="#FF4500",
            command=lambda oid=ogrenci_id: sil_ogrenci(oid)
        ).grid(row=i, column=10, padx=5, pady=5)

        ctk.CTkButton(
            scroll_frame, text="Ders İşlemleri", font=("Arial", 12), fg_color="#4682B4", hover_color="#4169E1",
            command=lambda oid=ogrenci_id: assignClassToStudent.ders_ekle_ogrenci(oid, scroll_frame)
        ).grid(row=i, column=11, padx=5, pady=5)

        ctk.CTkButton(
            scroll_frame, text="Öğretmen İşlemleri", font=("Arial", 12), fg_color="#4682B4", hover_color="#4169E1",
            command=lambda oid=ogrenci_id: assignClassToStudent.ders_ekle_ogrenci(oid, scroll_frame)
        ).grid(row=i, column=11, padx=5, pady=5)


