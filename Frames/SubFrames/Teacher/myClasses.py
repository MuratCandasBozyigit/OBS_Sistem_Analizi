import customtkinter as ctk
from DB.Migrations.ModelBuilder.TeacherCourse import ogretmenin_derslerini_getir
from . import myStudents

def Classes(ogretmen_id):
    dersler = ogretmenin_derslerini_getir(ogretmen_id)

    # root yerine toplevel kullanılabilir, uygulamaya bağlı
    root = ctk.CTk()
    root.title("Öğretmen Ders Listesi")
    root.geometry("600x500")

    frame = ctk.CTkFrame(root)
    frame.pack(padx=20, pady=20, fill="both", expand=True)

    ctk.CTkLabel(frame, text=f"Öğretmen ID: {ogretmen_id} - Atanmış Dersler", font=("Arial", 16)).pack(pady=10)

    ders_frame = ctk.CTkFrame(frame)
    ders_frame.pack(fill="both", expand=True, padx=10, pady=10)

    if not dersler:
        ctk.CTkLabel(ders_frame, text="Bu öğretmene atanmış ders yok.").pack(pady=10)
    else:
        max_columns = 4
        for index, (ders_id, ders_adi) in enumerate(dersler):
            row = index // max_columns
            column = index % max_columns

            ders_button = ctk.CTkButton(
                ders_frame,
                text=f"{ders_id}\n{ders_adi}",
                font=("Arial", 12),
                fg_color="#2a2a2a",
                hover_color="#3a3a3a",
                corner_radius=10,
                height=60,
                width=120,
                text_color="white",
                command=lambda d=ders_id: myStudents.students(d)
            )
            ders_button.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

        for col in range(max_columns):
            ders_frame.grid_columnconfigure(col, weight=1)

    ctk.CTkButton(frame, text="Kapat", command=root.destroy).pack(pady=20)

    root.mainloop()
