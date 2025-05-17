import customtkinter as ctk
from DB.Migrations.ModelBuilder.StudentCourse import ogrencinin_derslerini_getir

def DersListesiSayfasi(ogrenci_id):
    # Ders verilerini al
    dersler = ogrencinin_derslerini_getir(ogrenci_id)

    # Arayüz penceresi
    root = ctk.CTk()
    root.title("Öğrenci Ders Listesi")
    root.geometry("400x400")

    # Frame
    frame = ctk.CTkFrame(root)
    frame.pack(padx=20, pady=20, fill="both", expand=True)

    # Başlık
    label = ctk.CTkLabel(frame, text=f"Öğrenci ID: {ogrenci_id} - Atanmış Dersler", font=("Arial", 16))
    label.pack(pady=(0, 10))

    # Dersler yoksa mesaj ver
    if not dersler:
        no_course_label = ctk.CTkLabel(frame, text="Bu öğrenciye atanmış ders yok.")
        no_course_label.pack(pady=10)
    else:
        # Dersleri listele
        for ders_id, ders_adi in dersler:
            ders_label = ctk.CTkLabel(frame, text=f"{ders_id} - {ders_adi}", anchor="w")
            ders_label.pack(fill="x", padx=10, pady=5)

    # Kapat butonu
    close_btn = ctk.CTkButton(frame, text="Kapat", command=root.destroy)
    close_btn.pack(pady=20)

    root.mainloop()
