import customtkinter as ctk
from DB.Migrations.Class.create import ders_ekle
from DB.Migrations.Class.update import ders_guncelle

def ders_ekleme_penceresi(guncelleme_modu=False, mevcut_ders=None):
    win = ctk.CTkToplevel()
    win.title("Ders Ekle / Güncelle")
    win.geometry("400x300")
    win.lift()
    win.attributes('-topmost', True)
    win.after(200, lambda: win.attributes('-topmost', False))

    ders_ekleme_sayfasi(win, guncelleme_modu, mevcut_ders)

def ders_ekleme_sayfasi(root_frame, guncelleme_modu=False, mevcut_ders=None):
    for widget in root_frame.winfo_children():
        widget.destroy()

    title = "Dersi Güncelle" if guncelleme_modu else "Yeni Ders Ekle"
    title_label = ctk.CTkLabel(root_frame, text=title, font=("Arial", 20, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

    # Ders Adı
    ders_adi_label = ctk.CTkLabel(root_frame, text="Ders Adı:")
    ders_adi_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    ders_adi_entry = ctk.CTkEntry(root_frame)
    ders_adi_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    # Ders Saati
    ders_saati_label = ctk.CTkLabel(root_frame, text="Ders Saati (1-30):")
    ders_saati_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
    ders_saati_entry = ctk.CTkEntry(root_frame)
    ders_saati_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    # Giriş validasyonu sadece klavyede işe yarar ama biz esas kontrolü kaydet'te yapıyoruz
    def validate_input(new_text):
        if not new_text:
            return True
        return new_text.isdigit()
    
    validation = root_frame.register(validate_input)
    ders_saati_entry.configure(validate="key", validatecommand=(validation, '%P'))

    # Önceden gelen değerleri yerleştir (güncelleme moduysa)
    if guncelleme_modu and mevcut_ders:
        ders_adi_entry.insert(0, mevcut_ders["adi"])
        ders_saati_entry.insert(0, str(mevcut_ders["saati"]))

    def reset_entry_styles():
        ders_adi_entry.configure(border_color="gray")
        ders_saati_entry.configure(border_color="gray")

    def kaydet():
        ders_adi = ders_adi_entry.get().strip()
        ders_saati_raw = ders_saati_entry.get().strip()
        reset_entry_styles()

        # Önceki mesajları temizle
        for widget in root_frame.grid_slaves(row=4):
            widget.destroy()

        # Validasyon
        errors = []

        if not ders_adi:
            ders_adi_entry.configure(border_color="red")
            errors.append("Ders adı boş olamaz")

        try:
            ders_saati = int(ders_saati_raw)
            if not (1 <= ders_saati <= 30):
                raise ValueError
        except:
            ders_saati_entry.configure(border_color="red")
            errors.append("Ders saati 1 ile 30 arasında bir sayı olmalıdır")

        if errors:
            mesaj = ctk.CTkLabel(root_frame, text="\n".join(errors), text_color="red")
            mesaj.grid(row=4, column=0, columnspan=2, pady=10)
            return

        # İşlem başarılı, ekleme ya da güncelleme yap
        try:
            if guncelleme_modu and mevcut_ders:
                ders_guncelle(mevcut_ders["id"], ders_adi, ders_saati)
                mesaj = ctk.CTkLabel(root_frame, text="Ders başarıyla güncellendi!", text_color="green")
            else:
                ders_ekle(ders_adi, ders_saati)
                mesaj = ctk.CTkLabel(root_frame, text="Ders başarıyla eklendi!", text_color="green")
                ders_adi_entry.delete(0, 'end')
                ders_saati_entry.delete(0, 'end')
        except Exception as e:
            mesaj = ctk.CTkLabel(root_frame, text=f"Hata: {str(e)}", text_color="red")

        mesaj.grid(row=4, column=0, columnspan=2, pady=10)

    btn_text = "Güncelle" if guncelleme_modu else "Kaydet"
    kaydet_button = ctk.CTkButton(root_frame, text=btn_text, command=kaydet)
    kaydet_button.grid(row=3, column=0, columnspan=2, pady=20)

    root_frame.grid_columnconfigure(0, weight=1)
    root_frame.grid_columnconfigure(1, weight=1)
