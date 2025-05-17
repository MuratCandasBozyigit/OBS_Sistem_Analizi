import customtkinter as ctk
from Login import session  # sadece current_user_id lazım

def teacher_gui():
    from . import myClasses
    from . import myStudents

    root = ctk.CTk()
    root.title("Murat Eğitim Bakanlığı\nÖğretmen İşleri")
    root.geometry("400x300")

    frame = ctk.CTkFrame(root)
    frame.pack(fill="both", expand=True, padx=20, pady=20)
    frame.grid_columnconfigure(0, weight=1)

    myclasses_button = ctk.CTkButton(
        frame,
        text="Eğitim Görevlisi Olduğum Dersler",
        width=200,
        height=50,
        command=lambda: myClasses.Classes(session.current_user_id)  # ← Doğru kullanım
    )
    myclasses_button.grid(row=0, column=0, pady=10)

    allStudents_button = ctk.CTkButton(
        frame,
        text="Eğitim verdiğim öğrenciler",
        width=200,
        height=50,
        command=lambda: myStudents.students(session.current_user_id)
    )
    allStudents_button.grid(row=1, column=0, pady=10)


    def on_enter(event, btn):
        btn.configure(fg_color="darkblue")

    def on_leave(event, btn):
        btn.configure(fg_color="gray")

    for button in [myclasses_button, allStudents_button]:
        button.bind("<Enter>", lambda e, b=button: on_enter(e, b))
        button.bind("<Leave>", lambda e, b=button: on_leave(e, b))

    root.mainloop()
