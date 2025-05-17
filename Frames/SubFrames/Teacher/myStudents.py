import customtkinter as ctk
from tkinter import messagebox
from DB.Migrations.ModelBuilder.TeacherStudent import ogretmenin_ogrencilerini_getir

def students(ogretmen_id):
    root = ctk.CTk()
    root.title("Öğretmene Atanmış Öğrenciler")
    root.geometry("700x500")

    frame = ctk.CTkFrame(root)
    frame.pack(padx=20, pady=20, fill="both", expand=True)

    title = ctk.CTkLabel(frame, text=f"Öğretmen ID: {ogretmen_id} - Atanmış Öğrenciler", font=("Arial", 16))
    title.pack(pady=(10, 10))

    content_frame = ctk.CTkFrame(frame)
    content_frame.pack(fill="both", expand=True, padx=10, pady=10)

    try:
        ogrenciler = ogretmenin_ogrencilerini_getir(ogretmen_id)
    except Exception as e:
        messagebox.showerror("Hata", f"Öğrenciler getirilemedi:\n{e}")
        root.destroy()
        return

    if not ogrenciler:
        label = ctk.CTkLabel(content_frame, text="Bu öğretmene atanmış öğrenci yok.")
        label.pack(pady=10)
    else:
        max_columns = 4
        for index, (ogrenci_id, adi, soyadi) in enumerate(ogrenciler):
            row = index // max_columns
            column = index % max_columns

            ogrenci_label = ctk.CTkButton(
                content_frame,
                text=f"{ogrenci_id}\n{adi} {soyadi}",
                font=("Arial", 12),
                fg_color="#2a2a2a",
                hover_color="#3a3a3a",
                text_color="white",
                corner_radius=10,
                height=60,
                width=150,
                state="disabled"  # tıklanamaz, sadece görsel amaçlı
            )
            ogrenci_label.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

        for col in range(max_columns):
            content_frame.grid_columnconfigure(col, weight=1)

    kapat_btn = ctk.CTkButton(frame, text="Kapat", command=root.destroy)
    kapat_btn.pack(pady=20)

    root.mainloop()
