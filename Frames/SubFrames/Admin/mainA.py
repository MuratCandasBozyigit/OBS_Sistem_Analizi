import customtkinter as ctk

def admin_gui():
    from Frames.SubFrames.Admin.Class import getClasses  
    from Frames.SubFrames.Admin.Student import getStudents
    from Frames.SubFrames.Admin.Teacher import getTeachers
    import Frames  # Ana sayfaya dönüş için gerekli

    root = ctk.CTk()
    root.title("Admin Paneli")
    root.geometry("400x400")

    frame = ctk.CTkFrame(root)
    frame.pack(fill="both", expand=True, padx=20, pady=20)
    frame.grid_columnconfigure(0, weight=1)

    # Butonlar
    addStudent_button = ctk.CTkButton(frame, text="Öğrenci İşlemleri", width=200, height=50,command=getStudents.ogrencileri_listele_gui )
    addStudent_button.grid(row=0, column=0, pady=10)

    addTeacher_button = ctk.CTkButton(frame, text="Öğretmen İşlemleri", width=200, height=50, )
    addTeacher_button.grid(row=1, column=0, pady=10)

    addClass_button = ctk.CTkButton(frame, text="Ders İşlemleri", width=200, height=50,
                                    command=getClasses.dersleri_listele_gui)
    addClass_button.grid(row=2, column=0, pady=10)

    back_button = ctk.CTkButton(frame, text="Ana Sayfaya Dön", command=lambda: [root.destroy(), Frames.build_gui()],
                                fg_color="gray")
    back_button.grid(row=3, column=0, pady=20)

    # Hover efektleri (butonların rengi üzerine gelince değişir)
    buttons = [addStudent_button, addTeacher_button, addClass_button, back_button]
    for button in buttons:
        button.bind("<Enter>", lambda e, b=button: b.configure(fg_color="#1e40af"))  # koyu mavi
        button.bind("<Leave>", lambda e, b=button: b.configure(fg_color="#3b82f6"))  # normal mavi

    root.mainloop()
