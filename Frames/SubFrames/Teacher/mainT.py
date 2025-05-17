import customtkinter as ctk



def teacher_gui():
    from . import students
    from . import myClasses
    from . import examScores
    # Ana pencereyi oluşturuyoruz
    root = ctk.CTk()
    root.title("Ana Sayfa")
    root.geometry("400x300")

    # Ana frame
    frame = ctk.CTkFrame(root)
    frame.pack(fill="both", expand=True, padx=20, pady=20)
    frame.grid_columnconfigure(0, weight=1)

    # # Butonları oluşturuyoruz
    # myClasses_button = ctk.CTkButton(
    #     frame,
    #     text="Eğitim Görevlisi Olduğum Dersler",
    #     width=200,
    #     height=50,
    #     command=myClasses.myClasses
    # )
    # myClasses_button.grid(row=0, column=0, pady=10)

    # allStudents_button = ctk.CTkButton(
    #     frame,
    #     text="Tüm Öğrenciler",
    #     width=200,
    #     height=50,
    #     command=students.students
    # )
    # allStudents_button.grid(row=1, column=0, pady=10)

    # examScores_button = ctk.CTkButton(
    #     frame,
    #     text="Sınav Notları",
    #     width=200,
    #     height=50,
    #     command=examScores.examScores
    # )
    # examScores_button.grid(row=2, column=0, pady=10)

    # Hover efekt fonksiyonları
    def on_enter(event, btn):
        btn.configure(fg_color="darkblue")

    def on_leave(event, btn):
        btn.configure(fg_color="gray")

    # for button in [ allStudents_button, examScores_button]:
    #     button.bind("<Enter>", lambda e, b=button: on_enter(e, b))
    #     button.bind("<Leave>", lambda e, b=button: on_leave(e, b))

    root.mainloop()