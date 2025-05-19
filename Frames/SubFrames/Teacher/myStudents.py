import customtkinter as ctk
from tkinter import messagebox
from DB.Migrations.ModelBuilder.StudentCourse import dersi_alan_ogrencileri_getir
from DB.Migrations.ModelBuilder.examScores import not_ekle_veya_guncelle, notlari_getir

def students(ders_id):
    root = ctk.CTk()
    root.title(f"Ders ID: {ders_id} - Kayıtlı Öğrenciler")
    root.geometry("700x400")

    frame = ctk.CTkFrame(root)
    frame.pack(padx=10, pady=10, fill="both", expand=True)

    title = ctk.CTkLabel(frame, text=f"Ders ID: {ders_id} - Kayıtlı Öğrenciler", font=ctk.CTkFont("Arial", 14))
    title.pack(pady=(5, 10))

    content_frame = ctk.CTkFrame(frame)
    content_frame.pack(fill="both", expand=True, padx=5, pady=5)

    try:
        ogrenciler = dersi_alan_ogrencileri_getir(ders_id)
    except Exception as e:
        messagebox.showerror("Hata", f"Öğrenciler getirilemedi:\n{e}")
        root.destroy()
        return

    if not ogrenciler:
        label = ctk.CTkLabel(content_frame, text="Bu derse kayıtlı öğrenci yok.", text_color="red", font=ctk.CTkFont("Arial", 12))
        label.pack(pady=10)
    else:
        max_columns = 3

        def not_sayfasini_ac(ogrenci_id, adi, soyadi):
            pencere = ctk.CTkToplevel(root)
            pencere.title("Not Girme Sayfası")
            pencere.geometry("400x300")
            pencere.lift()
            pencere.attributes('-topmost', True)
            pencere.after(200, lambda: pencere.attributes('-topmost', False))

            baslik = ctk.CTkLabel(
                pencere, 
                text=f"{adi} {soyadi} (ID: {ogrenci_id})", 
                font=ctk.CTkFont("Arial", 14, "bold")
            )
            baslik.pack(pady=15)

            main_frame = ctk.CTkFrame(pencere)
            main_frame.pack(padx=20, pady=10, fill="both", expand=True)

            vize_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
            vize_frame.pack(pady=5, fill="x")
            ctk.CTkLabel(vize_frame, text="Vize Notu:").pack(side="left")
            vize_entry = ctk.CTkEntry(vize_frame)
            vize_entry.pack(side="right", padx=10)

            final_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
            final_frame.pack(pady=5, fill="x")
            ctk.CTkLabel(final_frame, text="Final Notu:").pack(side="left")
            final_entry = ctk.CTkEntry(final_frame)
            final_entry.pack(side="right", padx=10)

            kaydet_btn = ctk.CTkButton(
                main_frame, 
                text="Kaydet", 
                command=lambda: kaydet(vize_entry, final_entry, ogrenci_id, ders_id, pencere)
            )
            kaydet_btn.pack(pady=20)

            mevcut_notlar = notlari_getir(ogrenci_id, ders_id)
            if mevcut_notlar:
                vize_entry.insert(0, str(mevcut_notlar[0] or ""))
                final_entry.insert(0, str(mevcut_notlar[1] or ""))
            else:
                vize_entry.insert(0, "0")
                final_entry.insert(0, "0")

        def kaydet(vize_entry, final_entry, ogrenci_id, ders_id, pencere):
            try:
                vize = vize_entry.get()
                final = final_entry.get()

                if not vize or not final:
                    messagebox.showerror("Hata", "Vize ve Final notları boş olamaz!")
                    return

                vize = float(vize) if vize.replace('.', '', 1).isdigit() else None
                final = float(final) if final.replace('.', '', 1).isdigit() else None
                
                if vize is None or final is None:
                    messagebox.showerror("Hata", "Lütfen geçerli sayılar girin!")
                    return

                if not (0 <= vize <= 100) or not (0 <= final <= 100):
                    messagebox.showerror("Hata", "Notlar 0 ile 100 arasında olmalıdır!")
                    return

                not_ekle_veya_guncelle(ogrenci_id, ders_id, vize, final)
                messagebox.showinfo("Başarılı", "Notlar kaydedildi!")
                pencere.destroy()

            except Exception as e:
                messagebox.showerror("Hata", f"Bir hata oluştu: {e}")

        for index, (ogrenci_id, adi, soyadi) in enumerate(ogrenciler):
            row = index // max_columns
            column = index % max_columns

            kart = ctk.CTkFrame(content_frame, fg_color="#2a2a2a", corner_radius=8)
            kart.grid(row=row, column=column, padx=8, pady=8, sticky="n")

            def yaz_parca(parent, etiket, veri):
                satir = ctk.CTkFrame(parent, fg_color="transparent")
                satir.pack(padx=8, pady=2)
                ctk.CTkLabel(satir, text=etiket, text_color="red", font=ctk.CTkFont("Arial", 10, "bold")).pack(side="left")
                ctk.CTkLabel(satir, text=veri, text_color="white", font=ctk.CTkFont("Arial", 10)).pack(side="left", padx=(0, 8))

            yaz_parca(kart, "ID: ", str(ogrenci_id))
            yaz_parca(kart, "Ad: ", adi)
            yaz_parca(kart, "Soyad: ", soyadi)

            notver_btn = ctk.CTkButton(kart, text="Not Ver", height=26, command=lambda oid=ogrenci_id, a=adi, s=soyadi: not_sayfasini_ac(oid, a, s))
            notver_btn.pack(pady=(5, 10))

        for col in range(max_columns):
            content_frame.grid_columnconfigure(col, weight=1)

    ctk.CTkButton(frame, text="Kapat", command=root.destroy, height=32, width=80).pack(pady=10)
    root.mainloop()
