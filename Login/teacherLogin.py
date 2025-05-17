import customtkinter as ctk
import sqlite3
import os
DB_PATH = os.path.join(os.getcwd(), "okul.db")
def teacherLogin():
    from Frames.startFrame import build_gui
    root = ctk.CTk()
    root.title("Öğretmen Giriş Sayfası")
    root.geometry("400x400")

    frame = ctk.CTkFrame(root)
    frame.pack(padx=30, pady=30, fill="both", expand=True)

    title = ctk.CTkLabel(frame, text="Öğretmen Giriş", font=("Arial", 20))
    title.pack(pady=(10, 20))

    _name = ctk.CTkEntry(frame, placeholder_text="Ad")
    _name.pack(pady=10)
    sur_name = ctk.CTkEntry(frame, placeholder_text="Soyad")
    sur_name.pack(pady=10)
    tckn_entry = ctk.CTkEntry(frame, placeholder_text="TCKN", show="*")
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
                SELECT * FROM ogretmenler
                WHERE ogretmen_adı=? AND ogretmen_soyadı=? AND ogretmen_tckn=?
            ''', (ad, soyad, sifre))
            
            admin = cursor.fetchone()
            conn.close()

            if admin:
                login_status.configure(text="Giriş başarılı!", text_color="green")
                root.after(500, lambda: [root.destroy(), open_teacher_gui()])
            else:
                login_status.configure(text="Bilgiler hatalı!", text_color="red")

        except Exception as e:
            try:
                login_status.configure(text=f"Hata oluştu: {e}", text_color="red")
            except Exception:
                pass  # Label yoksa hata bastırılır

    def open_teacher_gui():
        from Frames.SubFrames.Teacher.mainT import teacher_gui
        teacher_gui()

    login_button = ctk.CTkButton(frame, text="Giriş Yap", command=login_action)
    login_button.pack(pady=20)

    def go_back():
        root.destroy()
        build_gui()

    back_button = ctk.CTkButton(frame, text="Geri Dön", command=go_back, fg_color="gray")
    back_button.pack(pady=5)

    root.mainloop()