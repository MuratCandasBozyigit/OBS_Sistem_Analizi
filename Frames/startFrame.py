import customtkinter as ctk
from Login.adminLogin import adminLogin
from Login.teacherLogin import teacherLogin
from Login.studentLogin import studentLogin

def build_gui():
    root = ctk.CTk()
    root.title("Murat Eğitim Bakanlığı")
    root.geometry("300x260")

    frame = ctk.CTkFrame(root)
    frame.pack(fill="both", expand=True, padx=20, pady=20)
    frame.grid_columnconfigure(0, weight=1)

    message_label = ctk.CTkLabel(frame, text="", text_color="black")
    message_label.grid(row=3, column=0, pady=20)

    def open_page(page):
        if page == "yon1":
            message_label.configure(text="Admin sayfasına yönlendiriliyor...")
            root.destroy()
            adminLogin()
        elif page == "yon2":
            message_label.configure(text="Öğretmen sayfasına yönlendiriliyor...")
            root.destroy()
            teacherLogin()
        elif page == "yon3":
            message_label.configure(text="Öğrenci sayfasına yönlendiriliyor...")
            root.destroy()
            studentLogin()

    admin_button = ctk.CTkButton(frame, text="Admin Girişi", width=200, height=50, command=lambda: open_page("yon1"))
    admin_button.grid(row=0, column=0, pady=10)

    teacher_button = ctk.CTkButton(frame, text="Öğretmen Girişi", width=200, height=50, command=lambda: open_page("yon2"))
    teacher_button.grid(row=1, column=0, pady=10)

    student_button = ctk.CTkButton(frame, text="Öğrenci Girişi", width=200, height=50, command=lambda: open_page("yon3"))
    student_button.grid(row=2, column=0, pady=10)

    for button in [admin_button, teacher_button, student_button]:
        button.bind("<Enter>", lambda e, b=button: b.configure(fg_color="darkblue"))
        button.bind("<Leave>", lambda e, b=button: b.configure(fg_color="gray"))

    root.mainloop()
