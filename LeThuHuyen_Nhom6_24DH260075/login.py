import tkinter as tk
from tkinter import messagebox
import taotk

# Create main window
root = tk.Tk()
root.title("Login")
root.geometry("300x200")

# Add a label
label = tk.Label(root, text="Đăng nhập", font=("Arial", 20))
label.pack(pady=10)
lib_user = tk.Label(root, text="Username:")
lib_user.place(x=20, y=60)

lib_pass = tk.Label(root, text="Password:")
lib_pass.place(x=20, y=100)

entry_username = tk.Entry(root)
entry_username.place(x=90, y=60)

entry_password = tk.Entry(root, show="*")
entry_password.place(x=90, y=100)

def login():
    messagebox.showinfo("Login Info", f"Username: {entry_username.get()}\nPassword: {entry_password.get()}")
def tao_tk():
    root.destroy()
    taotk.show()
btn = tk.Button(root, text="Tạo tài khoản", command=tao_tk)
btn.place(x=40, y=140)

btn = tk.Button(root, text="Đăng nhập", command=login)
btn.place(x=160, y=140)

root.mainloop()