import customtkinter as ctk
from DB.Migrations.ModelBuilder.StudentCourse import ogrencinin_derslerini_getir
from DB.Migrations.ModelBuilder.examScores import notlari_getir

def DersListesiSayfasi(ogrenci_id):
    # Ders verilerini al
    dersler = ogrencinin_derslerini_getir(ogrenci_id)

    # Ana pencere
    root = ctk.CTk()
    root.title("Öğrenci Ders Listesi")
    root.geometry("800x600")  # Boyutu biraz büyüttük

    # Ana çerçeve
    frame = ctk.CTkFrame(root)
    frame.pack(padx=20, pady=20, fill="both", expand=True)

    # Başlık
    label = ctk.CTkLabel(frame, text=f"Öğrenci ID: {ogrenci_id} - Dersler ve Notlar", font=("Arial", 16, "bold"))
    label.pack(pady=(10, 20))

    # Ders kutularını barındıracak iç çerçeve
    ders_frame = ctk.CTkFrame(frame)
    ders_frame.pack(fill="both", expand=True, padx=10, pady=10)

    if not dersler:
        no_course_label = ctk.CTkLabel(ders_frame, text="Bu öğrenciye atanmış ders yok.")
        no_course_label.pack(pady=10)
    else:
        # Başlık satırı
        headers = ["Ders ID", "Ders Adı", "Vize", "Final", "Ortalama", "Harf Notu"]
        for col, header in enumerate(headers):
            header_label = ctk.CTkLabel(ders_frame, text=header, font=("Arial", 12, "bold"), text_color="#1e90ff")
            header_label.grid(row=0, column=col, padx=5, pady=5, sticky="ew")

        # Not hesaplama fonksiyonu
        def hesapla_ortalama(vize, final):
            if vize is None or final is None:
                return None
            return round(vize * 0.3 + final * 0.7, 2)

        def harf_notu_hesapla(ortalama):
            if ortalama is None:
                return "-"
            if ortalama >= 90: return "AA"
            elif ortalama >= 85: return "BA"
            elif ortalama >= 80: return "BB"
            elif ortalama >= 75: return "CB"
            elif ortalama >= 70: return "CC"
            elif ortalama >= 65: return "DC"
            elif ortalama >= 60: return "DD"
            elif ortalama >= 50: return "FD"
            else: return "FF"

        # Dersleri ve notları listele
        for row, (ders_id, ders_adi) in enumerate(dersler, start=1):
            # Notları getir
            notlar = notlari_getir(ogrenci_id, ders_id)
            vize = notlar[0] if notlar and notlar[0] is not None else None
            final = notlar[1] if notlar and notlar[1] is not None else None
            ortalama = hesapla_ortalama(vize, final)
            harf_notu = harf_notu_hesapla(ortalama)

            # Ders ID
            ders_id_label = ctk.CTkLabel(ders_frame, text=str(ders_id))
            ders_id_label.grid(row=row, column=0, padx=5, pady=5)

            # Ders Adı
            ders_adi_label = ctk.CTkLabel(ders_frame, text=ders_adi)
            ders_adi_label.grid(row=row, column=1, padx=5, pady=5)

            # Vize
            vize_label = ctk.CTkLabel(ders_frame, text=str(vize) if vize is not None else "-")
            vize_label.grid(row=row, column=2, padx=5, pady=5)

            # Final
            final_label = ctk.CTkLabel(ders_frame, text=str(final) if final is not None else "-")
            final_label.grid(row=row, column=3, padx=5, pady=5)

            # Ortalama
            ortalama_label = ctk.CTkLabel(ders_frame, text=str(ortalama) if ortalama is not None else "-")
            ortalama_label.grid(row=row, column=4, padx=5, pady=5)

            # Harf Notu
            harf_label = ctk.CTkLabel(ders_frame, text=harf_notu, 
                                    font=("Arial", 12, "bold"),
                                    text_color="#ff6347" if harf_notu in ["FD", "FF"] else "#2e8b57")
            harf_label.grid(row=row, column=5, padx=5, pady=5)

        # Sütun genişliklerini ayarla
        for col in range(len(headers)):
            ders_frame.grid_columnconfigure(col, weight=1)

    # Kapat butonu
    close_btn = ctk.CTkButton(frame, text="Kapat", command=root.destroy, fg_color="#ff6347", hover_color="#ff4500")
    close_btn.pack(pady=20)

    root.mainloop()