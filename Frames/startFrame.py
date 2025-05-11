# gui.py
import customtkinter as ctk

# Ana pencereyi oluştur
def build_gui():
    # Ana pencere
    root = ctk.CTk()
    root.title("Login Paneli")
    root.geometry("400x300")  # Ekran boyutunu ayarla

    # Dikey üçe bölen çerçeve
    frame = ctk.CTkFrame(root)
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Admin, Öğretmen ve Öğrenci butonları
    admin_button = ctk.CTkButton(frame, text="Admin Girişi", width=200, height=50, command=lambda: open_page("yon1"))
    admin_button.grid(row=0, column=0, pady=10)

    teacher_button = ctk.CTkButton(frame, text="Öğretmen Girişi", width=200, height=50, command=lambda: open_page("yon2"))
    teacher_button.grid(row=1, column=0, pady=10)

    student_button = ctk.CTkButton(frame, text="Öğrenci Girişi", width=200, height=50, command=lambda: open_page("yon3"))
    student_button.grid(row=2, column=0, pady=10)

    # Buton hover efektleri
    admin_button.bind("<Enter>", lambda e: admin_button.configure(fg_color="lightblue"))
    admin_button.bind("<Leave>", lambda e: admin_button.configure(fg_color="gray"))

    teacher_button.bind("<Enter>", lambda e: teacher_button.configure(fg_color="lightblue"))
    teacher_button.bind("<Leave>", lambda e: teacher_button.configure(fg_color="gray"))

    student_button.bind("<Enter>", lambda e: student_button.configure(fg_color="lightblue"))
    student_button.bind("<Leave>", lambda e: student_button.configure(fg_color="gray"))

    # Ekranı göster
    root.mainloop()

# Sayfa yönlendirmesini yapan fonksiyon
def open_page(page):
    if page == "yon1":
        print("Admin sayfasına yönlendiriliyor...")
        # yon1.py'yi aç
    elif page == "yon2":
        print("Öğretmen sayfasına yönlendiriliyor...")
        # yon2.py'yi aç
    elif page == "yon3":
        print("Öğrenci sayfasına yönlendiriliyor...")
        # yon3.py'yi aç
