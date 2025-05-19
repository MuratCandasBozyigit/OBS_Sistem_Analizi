import customtkinter as ctk
import sqlite3
import os
DB_PATH = os.path.join(os.getcwd(), "okul.db")

def adminLogin():
    from Frames.startFrame import build_gui
    root = ctk.CTk()
    root.title("Admin Giriş Sayfası")
    root.geometry("400x400")

    frame = ctk.CTkFrame(root)
    frame.pack(padx=30, pady=30, fill="both", expand=True)

    title = ctk.CTkLabel(frame, text="Admin Giriş", font=("Arial", 20))
    title.pack(pady=(10, 20))

    name_entry = ctk.CTkEntry(frame, placeholder_text="Ad Soyad")
    name_entry.pack(pady=10)

    username_entry = ctk.CTkEntry(frame, placeholder_text="Kullanıcı Adı")
    username_entry.pack(pady=10)

    password_entry = ctk.CTkEntry(frame, placeholder_text="Şifre", show="*")
    password_entry.pack(pady=10)

    login_status = ctk.CTkLabel(frame, text="", text_color="red")
    login_status.pack(pady=5)

    def login_action():
        ad_soyad = name_entry.get().strip()
        kullanici_adi = username_entry.get().strip()
        sifre = password_entry.get().strip()

        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()

            cursor.execute('''
                SELECT * FROM adminler
                WHERE ad_soyad=? AND kullanici_adi=? AND sifre=?
            ''', (ad_soyad, kullanici_adi, sifre))
            
            admin = cursor.fetchone()
            conn.close()

            if admin:
          #      session.current_user_id = ogrenci[0] 
                login_status.configure(text="Giriş başarılı!", text_color="green")
                root.destroy()
                from Frames.SubFrames.Admin.mainA import admin_gui
                admin_gui()
            else:
                login_status.configure(text="Bilgiler hatalı!", text_color="red")

        except Exception as e:
            login_status.configure(text=f"Hata oluştu: {e}", text_color="red")

    login_button = ctk.CTkButton(frame, text="Giriş Yap", command=login_action)
    login_button.pack(pady=0)

    def go_back():
        root.destroy()
        build_gui()

    back_button = ctk.CTkButton(frame, text="Geri Dön", command=go_back, fg_color="gray")
    back_button.pack(pady=10)

    root.mainloop()
