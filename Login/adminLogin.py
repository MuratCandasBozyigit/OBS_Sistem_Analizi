import customtkinter as ctk

def adminLogin():
    from Frames.startFrame import build_gui
    root = ctk.CTk()
    root.title("Admin Giriş Sayfası")
    root.geometry("400x400")


    frame = ctk.CTkFrame(root)
    frame.pack(padx=30, pady=30, fill="both", expand=True)

    title = ctk.CTkLabel(frame, text="Admin Giriş", font=("Arial", 20))
    title.pack(pady=(10, 20))

    full_name_entry = ctk.CTkEntry(frame, placeholder_text="Ad Soyad")
    full_name_entry.pack(pady=10)

    username_entry = ctk.CTkEntry(frame, placeholder_text="Kullanıcı Adı")
    username_entry.pack(pady=10)

    password_entry = ctk.CTkEntry(frame, placeholder_text="Şifre", show="*")
    password_entry.pack(pady=10)

    def login_action():
        print("Admin Ad Soyad:", full_name_entry.get())
        print("Kullanıcı Adı:", username_entry.get())
        print("Şifre:", password_entry.get())

        root.destroy()  
        from Frames.SubFrames.Admin.mainA import merhaba_ekran_a
        merhaba_ekran_a()  

    login_button = ctk.CTkButton(frame, text="Giriş Yap", command=login_action)
    login_button.pack(pady=20)

    def go_back():
        root.destroy()
        build_gui()

    back_button = ctk.CTkButton(frame, text="Geri Dön", command=go_back, fg_color="gray")
    back_button.pack(pady=5)


    root.mainloop()
