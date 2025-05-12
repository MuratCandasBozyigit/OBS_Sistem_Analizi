import customtkinter as ctk
from DB.Migrations.Class.read import tum_dersleri_getir

def dersleri_listele_gui():

    win = ctk.CTkToplevel()
    win.title("Ders Yönetimi")
    win.geometry("600x300") 

    # Başlık
    title = ctk.CTkLabel(win, text="Tüm Dersler", font=("Arial", 20, "bold"))  # master parametresi eklendi
    title.pack(pady=10)

    # Scrollable alan oluştur
    scroll_frame = ctk.CTkScrollableFrame(win, width=400, height=300)  # master parametresi eklendi
    scroll_frame.pack(padx=20, pady=10, fill="both", expand=True)

    # Verileri getir
    dersler = tum_dersleri_getir()

    if not dersler:
        ctk.CTkLabel(scroll_frame, text="Kayıtlı ders bulunamadı.", font=("Arial", 14)).pack(pady=5)
        return

    # Her dersi listele
    for ders in dersler:
        ders_id, ders_adi, ders_saati = ders
        ders_text = f"Ders ID: {ders_id} | Ders Adı: {ders_adi} | Saat: {ders_saati}"
        label = ctk.CTkLabel(scroll_frame, text=ders_text, font=("Arial", 14), anchor="w", justify="left")
        label.pack(padx=10, pady=5, fill="x")
