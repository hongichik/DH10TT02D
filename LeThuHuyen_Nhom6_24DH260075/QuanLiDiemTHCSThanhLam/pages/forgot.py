import tkinter as tk
from tkinter import messagebox
from common.button import CustomButton

class ForgotPage:
    def __init__(self, root, app):
        self.root = root
        self.app = app

        root.title("Quên mật khẩu")
        root.geometry("300x200")
        root.configure(bg="#e6f2ff")

        frame = tk.Frame(root, bg="white", padx=20, pady=20)
        frame.pack(pady=40)

        tk.Label(frame, text="Quên mật khẩu", bg="white").pack()

        self.user = tk.Entry(frame)
        self.user.pack(pady=5)

        CustomButton(frame, text="Lấy lại", command=self.fake).pack()
        CustomButton(frame, text="Quay lại", command=self.app.show_login).pack()

    def fake(self):
        messagebox.showinfo("Demo", "Chức năng demo 😆")