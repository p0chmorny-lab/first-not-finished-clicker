import customtkinter as ctk
from PIL import Image
oko = r"C:\Users\User\OneDrive\Pulpit\zajęcia\easyCLICKER\oczko.png"
ullepszenie = r"C:\Users\User\OneDrive\Pulpit\zajęcia\easyCLICKER\UPGRADE.png"
okoIMPEMENTACJA=ctk.CTkImage(dark_image=Image.open(oko), size=(100,100))
upgradeIMPLEMENTACJA=ctk.CTkImage(dark_image=Image.open(ullepszenie), size=(100, 100))
gra = ctk.CTk()
gra.title("Horripillant: Przebudzenie")
gra.geometry("1111x666")
backgroundIMAGE = r"C:\Users\User\OneDrive\Pulpit\zajęcia\easyCLICKER\bckgrnd1.png"
background = ctk.CTkImage(dark_image=Image.open(backgroundIMAGE), size=(1111, 666))
punkty = 0
ulepszenie = 1

ekran_tla = ctk.CTkLabel(
    master=gra,       # zrób tło i dodaj zamiast gra leniu
    text="", 
    
)
ekran_tla.place(x=0, y=0)

def kup_ulepszenie():
    global ulepszenie
    global punkty
    if punkty >= 10:
        ulepszenie = ulepszenie + 1
        punkty = punkty -10

        Punkty_ILOSC.configure(text=f"Punkty:{punkty}")
    else:
        print("ERROR BRAK PKT")


ctk.set_appearance_mode("dark")
def punkty_Dodaj():
    global punkty
    punkty += 1 * ulepszenie
    print(f"to twoje punkty: {punkty} a twój mnożnik to: {ulepszenie}")
    Punkty_ILOSC.configure(text=f"Punkty:{punkty}")


Punkty_ILOSC = ctk.CTkLabel(
    master=gra,       # zrób tło i dodaj zamiast gra leniu
    text=f"Punkty:{punkty}", 
    font=("Helvetica", 24, "bold")
)
# Punkty_ILOSC.place(relx=0.05, rely=0.05, anchor="center")
Punkty_ILOSC.pack(pady=20)



przycisk = ctk.CTkButton(
    master=gra,
    text="",
    image=okoIMPEMENTACJA,
    command=punkty_Dodaj,
    fg_color="transparent",
    hover_color="darkred",
)
przycisk.pack(pady=20)
    

Upgrade = ctk.CTkButton(
    master=gra,
    text="ULEPSZENIE X2",
    command=kup_ulepszenie,
    fg_color="transparent",
    hover_color="darkred",
    image=upgradeIMPLEMENTACJA,
    
)
Upgrade.pack(pady=20)
gra.mainloop()