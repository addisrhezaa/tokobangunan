import tkinter as tk
from tkinter import messagebox
import subprocess
import customtkinter
from PIL import Image
import os

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "owner" and password == "admin":
        messagebox.showinfo("Login", "Login berhasil!")
        subprocess.Popen(["python", "dashboard.py"])
        root.destroy()
    elif username == "karyawan" and password == "stok":
        messagebox.showinfo("Login", "Login berhasil!")
        subprocess.Popen(["python", "dashboard2.py"])
        root.destroy()
    else:
        messagebox.showerror("Login", "Username atau password salah!")

def label_clicked():
    messagebox.showwarning("Forgot Password", "Hubungi Owner")

def center_window(window, width, height):
    # Mendapatkan lebar dan tinggi layar
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Menghitung posisi x dan y untuk jendela agar berada di tengah layar
    x = int((screen_width/2) - (width/2))
    y = int((screen_height/2) - (height/2))

    # Menentukan posisi jendela
    root.geometry(f"{width}x{height}+{x}+{y}")
    root.resizable(False,False)

root=customtkinter.CTk(fg_color="#f4fc05")
root_width=500
root_height=350

file_path = os.path.dirname(os.path.realpath(__file__))

root.iconbitmap(file_path + '/Logo.ico')
root.title("UD Sriwijaya Karangploso")

image_login = customtkinter.CTkImage(Image.open(file_path + "/Logotype.png"), size=(230,80))

center_window(root, root_width, root_height)

frame=customtkinter.CTkFrame(master=root, fg_color="#FEF4DF", corner_radius=20,)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="",image=image_login, font=("Arial", 24))
label.pack(pady=10, padx=10)

entry_username=customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry_username.pack(pady=12, padx=10)

entry_password=customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry_password.pack(pady=12, padx=10)

button_login = customtkinter.CTkButton(master=frame, text="Login", command=login, fg_color="#FF8C52", hover_color="#72C822")
button_login.pack(pady=12, padx=10)

label_forgot=customtkinter.CTkLabel(master=frame, text="Forgot Password", cursor="hand2", text_color='blue', font=('Arial', 12,'underline'))
label_forgot.pack()

label_forgot.bind("<Button-1>", lambda event: label_clicked())

root.mainloop()
