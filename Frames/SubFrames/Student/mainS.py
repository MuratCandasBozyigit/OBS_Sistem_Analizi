import customtkinter as ctk


def yon2():
    print("Notlarım sayfasına yönlendiriliyor...")

def yon3():
    print("Yaklaşan Sınavlarım sayfasına yönlendiriliyor...")

def student_gui():
    # Ana pencereyi oluşturuyoruz
    root = ctk.CTk()
    root.title("Ana Sayfa")
    root.geometry("400x300")

    # Ana frame
    frame = ctk.CTkFrame(root)
    frame.pack(fill="both", expand=True, padx=20, pady=20)
    frame.grid_columnconfigure(0, weight=1)

    # Butonları oluşturuyoruz
    dersler_button = ctk.CTkButton(frame, text="Derslerim", width=200, height=50, )
    dersler_button.grid(row=0, column=0, pady=10)

    notlar_button = ctk.CTkButton(frame, text="Notlarım", width=200, height=50, command=yon2)
    notlar_button.grid(row=1, column=0, pady=10)

    sinavlar_button = ctk.CTkButton(frame, text="Yaklaşan Sınavlarım", width=200, height=50, command=yon3)
    sinavlar_button.grid(row=2, column=0, pady=10)

    # Butonlara hover efektleri ekliyoruz
    for button in [dersler_button, notlar_button, sinavlar_button]:
        button.bind("<Enter>", lambda e, b=button: b.configure(fg_color="darkblue"))
        button.bind("<Leave>", lambda e, b=button: b.configure(fg_color="gray"))

    root.mainloop()

