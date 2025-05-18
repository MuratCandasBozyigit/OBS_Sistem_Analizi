import customtkinter as ctk
from tkinter import messagebox
from DB.Migrations.ModelBuilder.TeacherStudent import ogretmenin_ogrencilerini_getir

def students(ogretmen_id):
    root = ctk.CTk()
    root.title("Öğretmene Atanmış Öğrenciler")
    root.geometry("700x400")

    frame = ctk.CTkFrame(root)
    frame.pack(padx=10, pady=10, fill="both", expand=True)

    title = ctk.CTkLabel(frame, text=f"Öğretmen ID: {ogretmen_id} - Atanmış Öğrenciler", font=ctk.CTkFont("Arial", 14))
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
        label = ctk.CTkLabel(content_frame, text="Bu öğretmene atanmış öğrenci yok.", text_color="red", font=ctk.CTkFont("Arial", 12))
        label.pack(pady=10)
    else:
        max_columns = 3
        popup = None  # popup referansı dışarıda tutuluyor

        def not_sayfasini_ac(ogrenci_id, adi, soyadi):
            pencere = ctk.CTkToplevel(root)
            pencere.title("Not Sayfası")
            pencere.geometry("400x400")
            pencere.lift()
            pencere.attributes('-topmost', True)
            pencere.after(200, lambda: pencere.attributes('-topmost', False))

            ctk.CTkLabel(pencere, text=f"Öğrenci ID: {ogrenci_id}", font=ctk.CTkFont("Arial", 12, "bold")).pack(pady=(10, 5))
            ctk.CTkLabel(pencere, text=f"Adı: {adi}", font=ctk.CTkFont("Arial", 12)).pack(pady=2)
            ctk.CTkLabel(pencere, text=f"Soyadı: {soyadi}", font=ctk.CTkFont("Arial", 12)).pack(pady=(2, 10))

            entries = {}
            for etiket in ["Vize 1", "Final"]:
                girdi_frame = ctk.CTkFrame(pencere, fg_color="transparent")
                girdi_frame.pack(pady=5, padx=20, fill="x")
                ctk.CTkLabel(girdi_frame, text=etiket, width=100, anchor="w").pack(side="left")
                entry = ctk.CTkEntry(girdi_frame, width=200)
                entry.pack(side="right", padx=10)
                entries[etiket] = entry

            def kaydet():
                print("Kaydedilen Notlar:")
                print(f"Öğrenci ID: {ogrenci_id}, Ad: {adi}, Soyad: {soyadi}")
                for etiket, entry in entries.items():
                    print(f"{etiket}: {entry.get()}")

            ctk.CTkButton(pencere, text="Kaydet", command=kaydet).pack(pady=20)

        def show_popup(event, x, y, ogrenci_id, adi, soyadi):
            nonlocal popup
            if popup:
                popup.destroy()

            popup = ctk.CTkFrame(content_frame, fg_color="#333", corner_radius=8)
            popup.place(x=x, y=y)

            popup_label = ctk.CTkLabel(popup, text="Seçenekler", font=ctk.CTkFont("Arial", 12, "bold"))
            popup_label.pack(padx=10, pady=(5, 0))

            ctk.CTkButton(popup, text="Not Sayfası", command=lambda: [not_sayfasini_ac(ogrenci_id, adi, soyadi), popup.destroy()], height=28).pack(padx=10, pady=8)

        for index, (ogrenci_id, adi, soyadi) in enumerate(ogrenciler):
            row = index // max_columns
            column = index % max_columns

            kart = ctk.CTkFrame(content_frame, fg_color="#2a2a2a", corner_radius=8)
            kart.grid(row=row, column=column, padx=8, pady=8, sticky="n")

            satir = ctk.CTkFrame(kart, fg_color="transparent")
            satir.pack(padx=8, pady=5)

            def yaz_parca(etiket, veri):
                ctk.CTkLabel(satir, text=etiket, text_color="red", font=ctk.CTkFont("Arial", 10, "bold")).pack(side="left")
                ctk.CTkLabel(satir, text=veri, text_color="white", font=ctk.CTkFont("Arial", 10)).pack(side="left", padx=(0, 8))

            yaz_parca("ID: ", str(ogrenci_id))
            yaz_parca("Ad: ", adi)
            yaz_parca("Soyad: ", soyadi)

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
