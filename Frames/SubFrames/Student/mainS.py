import customtkinter as ctk

def merhaba_ekran_s():
    # Ana pencereyi oluşturuyoruz
    pencere = ctk.CTk()
    pencere.geometry("200x200")  # Pencere boyutunu ayarlıyoruz

    # Merhaba yazan bir etiket ekliyoruz
    etiket = ctk.CTkLabel(pencere, text="Merhaba", font=("Arial", 24))
    etiket.pack(pady=50)  # Etiketi pencereye yerleştiriyoruz

    # Pencereyi gösteriyoruz
    pencere.mainloop()

# Fonksiyonu çağırarak pencereyi açabiliriz
merhaba_ekran_s()
