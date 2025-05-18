import customtkinter as ctk
from . import classes
from Login import session  # session'dan current_user_id'yi almak için

def student_gui():
    import Frames
    root = ctk.CTk()
    root.title("Ana Sayfa")
    root.geometry("300x200")

    # Ana frame
    frame = ctk.CTkFrame(root)
    frame.pack(fill="both", expand=True, padx=20, pady=20)
    frame.grid_columnconfigure(0, weight=1)

    # Butonları oluşturuyoruz, id'yi parametre olarak geçiriyoruz
    dersler_button = ctk.CTkButton(
        frame, text="Derslerim", width=200, height=50,
        command=lambda: classes.DersListesiSayfasi(session.current_user_id)
    )
    dersler_button.grid(row=0, column=0, pady=10)

    back_button = ctk.CTkButton(frame, text="Ana Sayfaya Dön", command=lambda: [root.destroy(), Frames.build_gui()],
                                fg_color="gray")
    back_button.grid(row=3, column=0, pady=20)
    # Butonlara hover efektleri ekliyoruz
    for button in [dersler_button]:
        button.bind("<Enter>", lambda e, b=button: b.configure(fg_color="darkblue"))
        button.bind("<Leave>", lambda e, b=button: b.configure(fg_color="gray"))

    root.mainloop()
