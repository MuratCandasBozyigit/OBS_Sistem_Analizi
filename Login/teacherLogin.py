import customtkinter as ctk

def teacherLogin():
    root = ctk.CTk()
    root.title("Öğretmen Giriş Sayfası")
    root.geometry("400x300")

    frame = ctk.CTkFrame(root)
    frame.pack(padx=30, pady=30, fill="both", expand=True)

    title = ctk.CTkLabel(frame, text="Öğretmen Giriş", font=("Arial", 20))
    title.pack(pady=(10, 20))

    tckn_entry = ctk.CTkEntry(frame, placeholder_text="TCKN")
    tckn_entry.pack(pady=10)

    password_entry = ctk.CTkEntry(frame, placeholder_text="Şifre", show="*")
    password_entry.pack(pady=10)

    def login_action():
        print("TCKN:", tckn_entry.get())
        print("Şifre:", password_entry.get())

    login_button = ctk.CTkButton(frame, text="Giriş Yap", command=login_action)
    login_button.pack(pady=20)

    root.mainloop()
