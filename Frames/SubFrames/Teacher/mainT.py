import customtkinter as ctk

# importlar fonksiyon içinde olmalı (circular import'u önlemek için)
def teacher_gui():
    from . import myClasses
    from . import myStudents
    from . import examScores

    root = ctk.CTk()
    root.title("Ana Sayfa")
    root.geometry("400x300")

    frame = ctk.CTkFrame(root)
    frame.pack(fill="both", expand=True, padx=20, pady=20)
    frame.grid_columnconfigure(0, weight=1)

    myclasses_button = ctk.CTkButton(
        frame,
        text="Eğitim Görevlisi Olduğum Dersler",
        width=200,
        height=50,
        command=myClasses.Classes
    )
    myclasses_button.grid(row=0, column=0, pady=10)

    allStudents_button = ctk.CTkButton(
        frame,
        text="Tüm Öğrenciler",
        width=200,
        height=50,
        command=myStudents.students
    )
    allStudents_button.grid(row=1, column=0, pady=10)

    examScores_button = ctk.CTkButton(
        frame,
        text="Sınav Notları",
        width=200,
        height=50,
        command=examScores.examScore
    )
    examScores_button.grid(row=2, column=0, pady=10)

    def on_enter(event, btn):
        btn.configure(fg_color="darkblue")

    def on_leave(event, btn):
        btn.configure(fg_color="gray")

    for button in [myclasses_button, allStudents_button, examScores_button]:
        button.bind("<Enter>", lambda e, b=button: on_enter(e, b))
        button.bind("<Leave>", lambda e, b=button: on_leave(e, b))

    root.mainloop()
