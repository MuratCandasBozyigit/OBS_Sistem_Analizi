import customtkinter as ctk
from DB.Migrations.ModelBuilder.TeacherCourse import ogretmenin_derslerini_getir

def Classes(ogretmen_id):
    # Ders verilerini al
    dersler = ogretmenin_derslerini_getir(ogretmen_id)

    # Ana pencere
    root = ctk.CTk()
    root.title("OGretmen Ders Listesi")
    root.geometry("600x500")

    # Ana çerçeve
    frame = ctk.CTkFrame(root)
    frame.pack(padx=20, pady=20, fill="both", expand=True)

    # Başlık
    label = ctk.CTkLabel(frame, text=f"Öğrenci ID: {ogretmen_id} - Atanmış Dersler", font=("Arial", 16))
    label.pack(pady=(10, 10))

    # Ders kutularını barındıracak iç çerçeve
    ders_frame = ctk.CTkFrame(frame)
    ders_frame.pack(fill="both", expand=True, padx=10, pady=10)

    if not dersler:
        no_course_label = ctk.CTkLabel(ders_frame, text="Bu öğrenciye atanmış ders yok.")
        no_course_label.pack(pady=10)
    else:
        max_columns = 4  # Her satıra 4 ders
        for index, (ders_id, ders_adi) in enumerate(dersler):
            row = index // max_columns
            column = index % max_columns

            # CTkButton ile hover efekti veriyoruz
            ders_button = ctk.CTkButton(
                ders_frame,
                text=f"{ders_id}\n{ders_adi}",
                font=("Arial", 12),
                fg_color="#2a2a2a",           # normal kutu rengi
                hover_color="#3a3a3a",        # üzerine gelince renk
                corner_radius=10,
                height=60,
                width=120,
                text_color="white"
            )
            ders_button.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

        for col in range(max_columns):
            ders_frame.grid_columnconfigure(col, weight=1)

    # Kapat butonu
    close_btn = ctk.CTkButton(frame, text="Kapat", command=root.destroy)
    close_btn.pack(pady=20)

    root.mainloop()
