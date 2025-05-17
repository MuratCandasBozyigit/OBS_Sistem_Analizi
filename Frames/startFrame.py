import customtkinter as ctk
from Login.adminLogin import adminLogin
from Login.teacherLogin import teacherLogin
from Login.studentLogin import studentLogin

def build_gui():
    # Ana pencereyi oluştur
    root = ctk.CTk()
    root.title("Murat Eğitim Bakanlığı")
    root.geometry("300x260")

    # Ana çerçeve
    frame = ctk.CTkFrame(root)
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Sayfa yönlendirmesi yapan fonksiyon
    def open_page(page):
        if page == "yon1":
            print("Admin sayfasına yönlendiriliyor...")
            root.destroy()
            adminLogin()
        elif page == "yon2":
            print("Öğretmen sayfasına yönlendiriliyor...")
            root.destroy()
            teacherLogin()
        elif page == "yon3":
            print("Öğrenci sayfasına yönlendiriliyor...")
            root.destroy()
            studentLogin()

    # Giriş butonlarını oluştur
    buttons = [
        ("Admin Girişi", "yon1"),
        ("Öğretmen Girişi", "yon2"),
        ("Öğrenci Girişi", "yon3")
    ]

    for i, (text, page) in enumerate(buttons):
        btn = ctk.CTkButton(frame, text=text, width=200, height=50, command=lambda p=page: open_page(p))
        btn.grid(row=i, column=0, pady=10)
        
        # Hover efektleri
        btn.bind("<Enter>", lambda e, b=btn: b.configure(fg_color="lightblue"))
        btn.bind("<Leave>", lambda e, b=btn: b.configure(fg_color="gray"))

    # Ana döngüyü başlat
    root.mainloop()
