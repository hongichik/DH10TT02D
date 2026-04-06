import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Đăng nhập")
root.geometry("320x260")
root.resizable(False, False)
root.configure(bg="#f5e8d3")   

# Tiêu đề
tk.Label(root, text="Đăng nhập", font=("Arial", 18, "bold"), bg="#f5e8d3").pack(pady=20)

# Username
tk.Label(root, text="Tên đăng nhập:", font=("Arial", 10), bg="#f5e8d3").place(x=40, y=80)
entry_user = tk.Entry(root, font=("Arial", 11), width=22)
entry_user.place(x=130, y=80)

# Password
tk.Label(root, text="Mật khẩu:", font=("Arial", 10), bg="#f5e8d3").place(x=40, y=120)
entry_pass = tk.Entry(root, show="*", font=("Arial", 11), width=22)
entry_pass.place(x=130, y=120)

def login():
    user = entry_user.get()
    pas = entry_pass.get()
    if user and pas:
        messagebox.showinfo("Đăng nhập", f"Username: {user}\nPassword: {pas}")
    else:
        messagebox.showwarning("Lỗi", "Vui lòng nhập đầy đủ thông tin!")

# Nút Đăng nhập
tk.Button(root, text="Đăng nhập", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white",
          width=12, command=login).place(x=50, y=180)

# Nút Tạo tài khoản
tk.Button(root, text="Tạo tài khoản", font=("Arial", 10), bg="#2196F3", fg="white",
          width=12).place(x=180, y=180)

root.mainloop()