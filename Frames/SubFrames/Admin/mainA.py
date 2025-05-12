import customtkinter as ctk

def yon1():
    print("Öğrenci kayıt sayfasına yönlendiriliyor...")

def yon2():
    print("Öğretmen kayıt sayfasına yönlendiriliyor...")

def yon3():
    print("Ders işlemleri sayfasına yönlendiriliyor...")

def admin_gui():
    import Frames
    root = ctk.CTk()
    root.title("Admin Paneli")
    root.geometry("400x500")

    frame = ctk.CTkFrame(root)
    frame.pack(fill="both", expand=True, padx=20, pady=20)
    frame.grid_columnconfigure(0, weight=1)

    addStudent_button = ctk.CTkButton(frame, text="Öğrenci Kayıt", width=200, height=50, command=yon1)
    addStudent_button.grid(row=0, column=0, pady=10)

    addTeacher_button = ctk.CTkButton(frame, text="Öğretmen Kayıt", width=200, height=50, command=yon2)
    addTeacher_button.grid(row=1, column=0, pady=10)

    addClass_button = ctk.CTkButton(frame, text="Yeni Ders Ekle", width=200, height=50, command=yon3)
    addClass_button.grid(row=2, column=0, pady=10)

    assignTeacher_button = ctk.CTkButton(frame, text="Derse Öğretmen Ata", width=200, height=50, command=yon3)
    assignTeacher_button.grid(row=3, column=0, pady=10)

    assignStudent_button = ctk.CTkButton(frame, text="Derse Öğrenci Ekle", width=200, height=50, command=yon3)
    assignStudent_button.grid(row=4, column=0, pady=10)

    def go_back():
        root.destroy()
        Frames.build_gui()

    back_button = ctk.CTkButton(frame, text="Ana Sayfaya Dön", command=go_back, fg_color="gray")
    back_button.grid(row=5, column=0, pady=10)

    # Hover efekti
    for button in [addStudent_button, addTeacher_button, addClass_button, assignTeacher_button, assignStudent_button]:
        button.bind("<Enter>", lambda e, b=button: b.configure(fg_color="darkblue"))
        button.bind("<Leave>", lambda e, b=button: b.configure(fg_color="blue"))

    root.mainloop()
