import customtkinter as ctk
from tkinter import messagebox
from DB.Migrations.Teacher import tum_ogretmenleri_getir, ogretmen_sil, ogretmen_guncelle
from . import createTeacher  # Öğretmen ekleme penceresini buradan çağırıyoruz
from . import assignClassToTeacher  # Ders atama sayfası
from . import assignStudentsToTeacher

def ogretmenleri_listele_gui():
    win = ctk.CTkToplevel()
    win.title("Öğretmen Yönetimi")
    win.geometry("1300x600") 
    win.lift()
    win.attributes('-topmost', True)
    win.after(200, lambda: win.attributes('-topmost', False))
    title = ctk.CTkLabel(win, text="Tüm Öğretmenler", font=("Arial", 22, "bold"))
    title.pack(pady=10)

    def refresh():
        win.destroy()
        ogretmenleri_listele_gui()

    button_frame = ctk.CTkFrame(win, fg_color="transparent")
    button_frame.pack(pady=(0, 10))

    yenile_btn = ctk.CTkButton(
        button_frame, text="Sayfayı Yenile 🔁", command=refresh,
        fg_color="gray", hover_color="darkgray", font=("Arial", 14)
    )
    yenile_btn.pack(side="left", padx=10)

    ekle_btn = ctk.CTkButton(
        button_frame, text="Yeni Öğretmen Ekle",
        command=createTeacher.ogretmen_ekleme_penceresi,
        fg_color="green", hover_color="#006400", font=("Arial", 14)
    )
    ekle_btn.pack(side="left", padx=10)

    scroll_frame = ctk.CTkScrollableFrame(win, width=1150, height=460)
    scroll_frame.pack(padx=20, pady=10, fill="both", expand=True)

    headers = ["ID", "Adı", "Soyadı", "Telefon", "TCKN", "Branş", "Adres", "   Güncelle","   Sil", "  Ders","  Öğrenci Ekle"]
    for col, header in enumerate(headers):
        ctk.CTkLabel(scroll_frame, text=header, font=("Arial", 15, "bold")).grid(
            row=0, column=col, padx=15, pady=5, sticky="w"
        )

    ogretmenler = tum_ogretmenleri_getir()
    if not ogretmenler:
        ctk.CTkLabel(scroll_frame, text="Kayıtlı öğretmen bulunamadı.", font=("Arial", 25, "bold")).grid(
            row=3, column=5, columnspan=10, pady=10
        )
        return

    guncelle_form = {"frame": None}

    def sil_ogretmen(ogretmen_id, frame):
        confirm = messagebox.askyesno("Öğretmeni Sil", f"ID: {ogretmen_id} olan öğretmeni silmek istiyor musunuz?")
        if confirm:
            try:
                ogretmen_sil(ogretmen_id)
                frame.destroy()
                messagebox.showinfo("Silindi", "Öğretmen başarıyla silindi.")
                refresh()
            except Exception as e:
                messagebox.showerror("Hata", f"Silinemedi!\n{e}")

    def guncelle_goster(row_idx, ogretmen_id, mevcut_ad, mevcut_soyad, mevcut_tel, mevcut_tckn, mevcut_brans, mevcut_adres):
        if guncelle_form["frame"]:
            guncelle_form["frame"].destroy()

        form = ctk.CTkFrame(scroll_frame, fg_color="#F0F0F0")
        form.grid(row=row_idx+1, column=0, columnspan=13, pady=(5, 15), sticky="ew", padx=10)

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
        entry_brans = add_label_entry(2, 1, "Branş:", mevcut_brans)
        entry_adres = add_label_entry(3, 1, "Adres:", mevcut_adres)

        def kaydet():
            yeni_ad = entry_ad.get().strip()
            yeni_soyad = entry_soyad.get().strip()
            yeni_tel = entry_tel.get().strip()
            yeni_tckn = entry_tckn.get().strip()
            yeni_brans = entry_brans.get().strip()
            yeni_adres = entry_adres.get().strip()

            if not all([yeni_ad, yeni_soyad, yeni_tel, yeni_tckn, yeni_brans, yeni_adres]):
                messagebox.showerror("Hata", "Alanlar boş bırakılamaz.")
                return

            try:
                ogretmen_guncelle(ogretmen_id, yeni_ad, yeni_soyad, yeni_adres, yeni_tel, yeni_tckn, yeni_brans)
                messagebox.showinfo("Başarılı", "Öğretmen güncellendi.")
                refresh()
            except Exception as e:
                messagebox.showerror("Hata", f"Güncelleme hatası:\n{e}")

        ctk.CTkButton(form, text="Kaydet", command=kaydet, width=100, fg_color="#FFA500", hover_color="#FF8C00").grid(row=4, column=4, padx=10)
        ctk.CTkButton(form, text="İptal", command=iptal_et, width=80, fg_color="gray", hover_color="darkgray").grid(row=4, column=5, padx=10, pady=5)

        guncelle_form["frame"] = form

    for i, ogretmen in enumerate(ogretmenler, start=1):
        ogretmen_id, ad, soyad, adres, tel, tckn, brans = ogretmen

        for idx, val in enumerate([ogretmen_id, ad, soyad, tel, tckn, brans, adres]):
            ctk.CTkLabel(scroll_frame, text=str(val), font=("Arial", 12)).grid(
                row=i, column=idx, padx=5, pady=5, sticky="w"
            )

        ctk.CTkButton(
            scroll_frame, text="Güncelle", font=("Arial", 12), fg_color="#FFA500", hover_color="#FF8C00",
            command=lambda row=i, oid=ogretmen_id, a=ad, s=soyad, t=tel, tc=tckn, b=brans, adr=adres:
            guncelle_goster(row, oid, a, s, t, tc, b, adr)
        ).grid(row=i, column=9, padx=5, pady=5)

        ctk.CTkButton(
            scroll_frame, text="Sil", font=("Arial", 12), fg_color="#FF6347", hover_color="#FF4500",
            command=lambda oid=ogretmen_id: sil_ogretmen(oid, scroll_frame)
        ).grid(row=i, column=10, padx=5, pady=5)

        ctk.CTkButton(
            scroll_frame, text="Ders Ekle", font=("Arial", 12), fg_color="#4682B4", hover_color="#4169E1",
            command=lambda oid=ogretmen_id: assignClassToTeacher.ders_ekle_ogretmen(oid, win)
        ).grid(row=i, column=11, padx=5, pady=5)

        ctk.CTkButton(
            scroll_frame, text="Öğrenci Ekle", font=("Arial", 12), fg_color="#4682B4", hover_color="#4169E1",
            command=lambda oid=ogretmen_id: assignStudentsToTeacher.ogrenci_ekle_ogretmen(oid, win)
        ).grid(row=i, column=12, padx=5, pady=5)
