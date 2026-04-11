import tkinter as tk
from tkinter import messagebox
import os
from common.button import CustomButton

class LoginPage:
    def __init__(self, root, app):
        self.root = root
        self.app = app

        root.title("Đăng nhập")
        root.geometry("350x300")
        root.configure(bg="#e6f2ff")

        frame = tk.Frame(root, bg="white", padx=20, pady=20)
        frame.pack(pady=40)

        tk.Label(frame, text="ĐĂNG NHẬP", bg="white", fg="#4da6ff", font=("Arial", 16, "bold")).pack()

        self.user = tk.Entry(frame)
        self.user.pack(pady=5)

        self.pw = tk.Entry(frame, show="*")
        self.pw.pack(pady=5)

        CustomButton(frame, text="Đăng nhập", command=self.login).pack(pady=5)
        CustomButton(frame, text="Đăng ký", command=self.app.show_register).pack()
        CustomButton(frame, text="Quên mật khẩu", command=self.app.show_forgot).pack()

    def login(self):
        if not os.path.exists("database/tk.csv"):
            messagebox.showerror("Lỗi", "Chưa có tài khoản")
            return

        with open("database/tk.csv", "r") as f:
            for line in f:
                data = line.strip().split(",")
                if len(data) >= 2:
                    if self.user.get() == data[0] and self.pw.get() == data[1]:
                        messagebox.showinfo("OK", "Đăng nhập thành công")
                        self.app.show_dashboard()
                        return

        messagebox.showerror("Sai", "Sai tài khoản")