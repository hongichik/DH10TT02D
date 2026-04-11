import tkinter as tk
from tkinter import messagebox
import os
from common.button import CustomButton

class RegisterPage:
    def __init__(self, root, app):
        self.root = root
        self.app = app

        root.title("Đăng ký")
        root.geometry("350x350")
        root.configure(bg="#e6f2ff")

        frame = tk.Frame(root, bg="white", padx=20, pady=20)
        frame.pack(pady=30)

        tk.Label(frame, text="ĐĂNG KÝ", bg="white", fg="#4da6ff", font=("Arial", 16, "bold")).pack()

        self.user = tk.Entry(frame)
        self.user.pack(pady=5)

        self.pw = tk.Entry(frame, show="*")
        self.pw.pack(pady=5)

        self.email = tk.Entry(frame)
        self.email.pack(pady=5)

        CustomButton(frame, text="Tạo tài khoản", command=self.register).pack(pady=5)
        CustomButton(frame, text="Quay lại", command=self.app.show_login).pack()

    def register(self):
        u = self.user.get()
        p = self.pw.get()
        e = self.email.get()

        if not u or not p or not e:
            messagebox.showerror("Lỗi", "Nhập thiếu")
            return

        if not os.path.exists("database"):
            os.makedirs("database")

        with open("database/tk.csv", "a") as f:
            f.write(f"{u},{p},{e}\n")

        messagebox.showinfo("OK", "Đăng ký thành công")
        self.app.show_dashboard()