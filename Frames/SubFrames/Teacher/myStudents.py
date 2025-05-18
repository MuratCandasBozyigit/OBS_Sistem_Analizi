import customtkinter as ctk
from tkinter import messagebox
from DB.Migrations.ModelBuilder.TeacherStudent import ogretmenin_ogrencilerini_getir

def students(ogretmen_id):
    root = ctk.CTk()
    root.title("Öğretmene Atanmış Öğrenciler")
    root.geometry("700x400")

    frame = ctk.CTkFrame(root)
    frame.pack(padx=10, pady=10, fill="both", expand=True)

    title = ctk.CTkLabel(frame, text=f"Öğretmen ID: {ogretmen_id} - Atanmış Öğrenciler", font=("Arial", 14))
    title.pack(pady=(5, 10))

    content_frame = ctk.CTkFrame(frame)
    content_frame.pack(fill="both", expand=True, padx=5, pady=5)

    try:
        ogrenciler = ogretmenin_ogrencilerini_getir(ogretmen_id)
    except Exception as e:
        messagebox.showerror("Hata", f"Öğrenciler getirilemedi:\n{e}")
        root.destroy()
        return

    if not ogrenciler:
        label = ctk.CTkLabel(content_frame, text="Bu öğretmene atanmış öğrenci yok.", text_color="red", font=("Arial", 12))
        label.pack(pady=10)
    else:
        max_columns = 3

        popup = None  # popup referansı dışarıda tutulsun

        def show_popup(event, x, y, ogrenci_id, adi, soyadi):
            nonlocal popup
            if popup:
                popup.destroy()

            popup = ctk.CTkFrame(content_frame, fg_color="#333", corner_radius=8)
            popup.place(x=x, y=y)

            popup_label = ctk.CTkLabel(popup, text="Seçenekler", font=("Arial", 12, "bold"))
            popup_label.pack(padx=10, pady=(5, 0))

            def not_sayfasina_git():
                print(f"NOT SAYFASI => ID: {ogrenci_id}, Ad: {adi}, Soyad: {soyadi}")
                popup.destroy()

            ctk.CTkButton(popup, text="Not Sayfası", command=not_sayfasina_git, height=28).pack(padx=10, pady=8)

        for index, (ogrenci_id, adi, soyadi) in enumerate(ogrenciler):
            row = index // max_columns
            column = index % max_columns

            kart = ctk.CTkFrame(content_frame, fg_color="#2a2a2a", corner_radius=8)
            kart.grid(row=row, column=column, padx=8, pady=8, sticky="n")

            satir = ctk.CTkFrame(kart, fg_color="transparent")
            satir.pack(padx=8, pady=5)

            def yaz_parca(etiket, veri):
                ctk.CTkLabel(satir, text=etiket, text_color="red", font=("Arial", 10, "bold")).pack(side="left")
                ctk.CTkLabel(satir, text=veri, text_color="white", font=("Arial", 10)).pack(side="left", padx=(0, 8))

            yaz_parca("ID: ", str(ogrenci_id))
            yaz_parca("Ad: ", adi)
            yaz_parca("Soyad: ", soyadi)

            # Hem tıklama hem hover için event ekle
            def bind_popup(widget, ogrenci_id, adi, soyadi):
                def handler(event):
                    show_popup(event, event.x_root - root.winfo_rootx(), event.y_root - root.winfo_rooty(), ogrenci_id, adi, soyadi)
                widget.bind("<Button-1>", handler)
                widget.bind("<Enter>", handler)

            bind_popup(kart, ogrenci_id, adi, soyadi)

        for col in range(max_columns):
            content_frame.grid_columnconfigure(col, weight=1)

    ctk.CTkButton(frame, text="Kapat", command=root.destroy, height=32, width=80).pack(pady=10)

    root.mainloop()
