import tkinter as tk
from common.button import CustomButton

class DashboardPage:
    def __init__(self, root, app):
        self.root = root
        self.app = app

        root.title("Quản lí điểm")
        root.geometry("400x250")
        root.configure(bg="#e6f2ff")

        frame = tk.Frame(root, bg="white", padx=20, pady=20)
        frame.pack(pady=40)

        tk.Label(frame, text="QUẢN LÍ ĐIỂM", bg="white", fg="#4da6ff", font=("Arial", 16)).pack()

        CustomButton(frame, text="Đăng xuất", command=self.app.show_login).pack(pady=10)