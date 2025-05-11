import customtkinter as ctk

def yon1():
    print("Derslerim sayfasına yönlendiriliyor...")

def yon2():
    print("Notlarım sayfasına yönlendiriliyor...")


def teacher_gui():
    # Ana pencereyi oluşturuyoruz
    root = ctk.CTk()
    root.title("Ana Sayfa")
    root.geometry("400x300")

    # Ana frame
    frame = ctk.CTkFrame(root)
    frame.pack(fill="both", expand=True, padx=20, pady=20)
    frame.grid_columnconfigure(0, weight=1)

    # Butonları oluşturuyoruz
    myClasses_button = ctk.CTkButton(frame, text="Eğitim Görevlisi Olduğum Dersler", width=200, height=50, command=yon1)
    myClasses_button.grid(row=0, column=0, pady=10)

    allStudents_button = ctk.CTkButton(frame, text="Tüm Öğrenciler", width=200, height=50, command=yon2)
    allStudents_button.grid(row=1, column=0, pady=10)

 

    # Butonlara hover efektleri ekliyoruz
    for button in [myClasses_button, allStudents_button]:
        button.bind("<Enter>", lambda e, b=button: b.configure(fg_color="darkblue"))
        button.bind("<Leave>", lambda e, b=button: b.configure(fg_color="gray"))

    root.mainloop()

