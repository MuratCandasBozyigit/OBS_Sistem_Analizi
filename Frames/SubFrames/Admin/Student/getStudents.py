import customtkinter as ctk
from tkinter import messagebox
from DB.Migrations.Student import tum_ogrencileri_getir, ogrenci_sil, ogrenci_guncelle
from . import createStudent, assignClassToStudent, assignTeacherToStudent

def ogrencileri_listele_gui():
    win = ctk.CTkToplevel()
    win.title("Öğrenci Yönetimi")
    win.geometry("1450x650")
    win.lift()
    win.attributes("-topmost", True)
    win.after(200, lambda: win.attributes("-topmost", False))

    ctk.CTkLabel(win, text="Tüm Öğrenciler", font=("Arial", 22, "bold")).pack(pady=10)

    def refresh():
        win.destroy()
        ogrencileri_listele_gui()

    # Üst butonlar
    button_frame = ctk.CTkFrame(win, fg_color="transparent")
    button_frame.pack(pady=5)

    ctk.CTkButton(button_frame, text="Sayfayı Yenile 🔁", command=refresh, fg_color="gray", hover_color="darkgray", font=("Arial", 14)).pack(side="left", padx=10)
    ctk.CTkButton(button_frame, text="Yeni Öğrenci Ekle", command=createStudent.ogrenci_ekleme_penceresi, fg_color="green", hover_color="#006400", font=("Arial", 14)).pack(side="left", padx=10)

    # Scrollable alan
    scroll_frame = ctk.CTkScrollableFrame(win, width=1300, height=460)
    scroll_frame.pack(padx=20, pady=10, fill="both", expand=True)

    headers = [
        "ID", "Adı", "Soyadı", "Telefon", "TCKN", "Numara",
        "Fotoğraf", "Adres", "Şifre",
        "Güncelle", "Sil", "Ders İşlemleri", "Öğretmen İşlemleri"
    ]
    for col, header in enumerate(headers):
        ctk.CTkLabel(scroll_frame, text=header, font=("Arial", 15, "bold")).grid(row=0, column=col, padx=5, pady=5, sticky="w")

    ogrenciler = tum_ogrencileri_getir()

    if not ogrenciler:
        ctk.CTkLabel(scroll_frame, text="Kayıtlı öğrenci bulunamadı.", font=("Arial", 18, "bold")).grid(row=1, column=0, columnspan=len(headers), pady=20)
        return

    guncelle_form = {"frame": None}

    def sil_ogrenci(ogrenci_id):
        if messagebox.askyesno("Öğrenci Sil", f"ID {ogrenci_id} olan öğrenciyi silmek istiyor musunuz?"):
            try:
                ogrenci_sil(ogrenci_id)
                messagebox.showinfo("Başarılı", "Öğrenci silindi.")
                refresh()
            except Exception as e:
                messagebox.showerror("Hata", f"Silme hatası:\n{e}")

    def guncelle_goster(row, ogrenci_id, *mevcut):
        if guncelle_form["frame"]:
            guncelle_form["frame"].destroy()

        form = ctk.CTkFrame(scroll_frame, fg_color="#F0F0F0")
        form.grid(row=row+1, column=0, columnspan=15, pady=10, padx=10, sticky="ew")

        labels = ["Adı", "Soyadı", "Telefon", "TCKN", "Numara", "Fotoğraf", "Adres", "Şifre"]
        entries = []
        for idx, (label, value) in enumerate(zip(labels, mevcut)):
            ctk.CTkLabel(form, text=label + ":", font=("Arial", 13)).grid(row=idx//2, column=(idx%2)*2, padx=5, pady=5, sticky="w")
            ent = ctk.CTkEntry(form, width=200, show="*" if label == "Şifre" else None)
            ent.insert(0, str(value) if value is not None else "")
            ent.grid(row=idx//2, column=(idx%2)*2 + 1, padx=5, pady=5)
            entries.append(ent)

        def kaydet():
            try:
                values = [e.get().strip() for e in entries]
                if not all(values):
                    messagebox.showerror("Hata", "Tüm alanlar doldurulmalıdır.")
                    return
                ogrenci_guncelle(ogrenci_id, *values)
                messagebox.showinfo("Başarılı", "Öğrenci güncellendi.")
                refresh()
            except Exception as e:
                messagebox.showerror("Hata", f"Güncelleme hatası:\n{e}")

        ctk.CTkButton(form, text="Kaydet", command=kaydet, fg_color="#FFA500", hover_color="#FF8C00").grid(row=5, column=3, padx=10)
        ctk.CTkButton(form, text="İptal", command=lambda: form.destroy(), fg_color="gray", hover_color="darkgray").grid(row=6, column=3, padx=10)

        guncelle_form["frame"] = form

    # Öğrenci satırlarını oluştur
    for i, ogr in enumerate(ogrenciler, start=1):
        ogr_id, ad, soyad, foto, adres, tel, tckn, numara, sifre ,vize,final = ogr

        row_data = [ogr_id, ad, soyad, tel, tckn, numara, foto, adres, sifre]
        for j, val in enumerate(row_data):
            ctk.CTkLabel(scroll_frame, text=str(val), font=("Arial", 12)).grid(row=i, column=j, padx=5, pady=5, sticky="w")

        ctk.CTkButton(scroll_frame, text="Güncelle", font=("Arial", 12), fg_color="#FFA500", hover_color="#FF8C00",
                      command=lambda i=i, oid=ogr_id: guncelle_goster(i, oid, ad, soyad, tel, tckn, numara, foto, adres, sifre)
                      ).grid(row=i, column=9, padx=5, pady=5)

        ctk.CTkButton(scroll_frame, text="Sil", font=("Arial", 12), fg_color="#FF6347", hover_color="#FF4500",
                      command=lambda oid=ogr_id: sil_ogrenci(oid)
                      ).grid(row=i, column=10, padx=5, pady=5)

        ctk.CTkButton(scroll_frame, text="Ders İşlemleri", font=("Arial", 12), fg_color="#4682B4", hover_color="#4169E1",
                      command=lambda oid=ogr_id: assignClassToStudent.ders_ekle_ogrenci(oid, scroll_frame)
                      ).grid(row=i, column=11, padx=5, pady=5)

        ctk.CTkButton(scroll_frame, text="Öğretmen İşlemleri", font=("Arial", 12), fg_color="#4682B4", hover_color="#4169E1",
                      command=lambda oid=ogr_id: assignTeacherToStudent.ogretmen_ekle_ogrenci(oid, scroll_frame)
                      ).grid(row=i, column=12, padx=5, pady=5)
