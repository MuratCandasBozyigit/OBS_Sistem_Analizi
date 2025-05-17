import customtkinter as ctk
import sqlite3
import os

DB_PATH = os.path.join(os.getcwd(), "okul.db")
def studentLogin():
    from Frames.startFrame import build_gui  # ← Fonksiyonun içine taşıdık

    root = ctk.CTk()
    root.title("Öğrenci Giriş Sayfası")
    root.geometry("400x400")

    frame = ctk.CTkFrame(root)
    frame.pack(padx=30, pady=30, fill="both", expand=True)

    title = ctk.CTkLabel(frame, text="Öğrenci Giriş", font=("Arial", 20))
    title.pack(pady=(10, 20))

    _name = ctk.CTkEntry(frame, placeholder_text="Ogrenci Adı", show="*")
    _name.pack(pady=10)

    sur_name = ctk.CTkEntry(frame, placeholder_text="Ogrenci Adı", show="*")
    sur_name.pack(pady=10)
    tckn_entry = ctk.CTkEntry(frame, placeholder_text="TCKN")
    tckn_entry.pack(pady=10)

    login_status = ctk.CTkLabel(frame, text="", text_color="red")
    login_status.pack(pady=5)

    def login_action():
        ad = _name.get().strip()
        soyad = sur_name.get().strip()
        sifre = tckn_entry.get().strip()

        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()

            cursor.execute('''
                SELECT * FROM adminler
                WHERE ad_sooyad=? AND kullanici_adi=? AND sifre=?
            ''', (ad, soyad, sifre))
            
            admin = cursor.fetchone()
            conn.close()

            if admin:
                login_status.configure(text="Giriş başarılı!", text_color="green")
                root.destroy()
                from Frames.SubFrames.Admin.mainA import admin_gui
                admin_gui()
            else:
                login_status.configure(text="Bilgiler hatalı!", text_color="red")

        except Exception as e:
            login_status.configure(text=f"Hata oluştu: {e}", text_color="red")

    login_button = ctk.CTkButton(frame, text="Giriş Yap", command=login_action)
    login_button.pack(pady=20)

    def go_back():
        root.destroy()
        build_gui()

    back_button = ctk.CTkButton(frame, text="Geri Dön", command=go_back, fg_color="gray")
    back_button.pack(pady=5)

    root.mainloop()
