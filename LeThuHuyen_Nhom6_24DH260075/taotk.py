import tkinter as tk
from tkinter import messagebox, font

class RegisterUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ thống - Tạo tài khoản")
        self.root.geometry("450x500")
        self.root.configure(bg="#ffd6e7")  # Nền hồng

        # Font
        self.title_font = font.Font(family="Helvetica", size=20, weight="bold")
        self.label_font = font.Font(family="Helvetica", size=10)
        self.entry_font = font.Font(family="Helvetica", size=11)

        self.setup_ui()

    def setup_ui(self):
        # Khung chính (trắng)
        self.main_container = tk.Frame(self.root, bg="#ffffff", bd=0)
        self.main_container.place(relx=0.5, rely=0.5, anchor="center")

        # Tiêu đề
        tk.Label(
            self.main_container,
            text="ĐĂNG KÝ",
            font=self.title_font,
            bg="#ffffff",
            fg="#d63384"  # hồng đậm
        ).pack(pady=(20, 20))

        # Input
        self.create_input_field("Tên đăng nhập:", "user")
        self.create_input_field("Email:", "email")
        self.create_input_field("Mật khẩu:", "pass", is_password=True)
        self.create_input_field("Xác nhận mật khẩu:", "confirm", is_password=True)

        # Nút đăng ký (hồng đậm)
        self.reg_btn = tk.Button(
            self.main_container,
            text="TẠO TÀI KHOẢN",
            command=self.validate_registration,
            bg="#ff69b4",
            fg="white",
            font=("Helvetica", 10, "bold"),
            padx=20,
            pady=10,
            cursor="hand2",
            bd=0,
            width=20,
            activebackground="#ff85c1"
        )
        self.reg_btn.pack(pady=20)

        # Link quay lại
        self.back_link = tk.Label(
            self.main_container,
            text="Đã có tài khoản? Đăng nhập ngay",
            bg="#ffffff",
            fg="#ff69b4",
            cursor="hand2",
            font=("Helvetica", 9, "underline")
        )
        self.back_link.pack(pady=(0, 20))

    def create_input_field(self, label_text, attr_name, is_password=False):
        frame = tk.Frame(self.main_container, bg="#ffffff")
        frame.pack(fill="x", padx=20, pady=5)

        tk.Label(
            frame,
            text=label_text,
            font=self.label_font,
            bg="#ffffff",
            anchor="w"
        ).pack(fill="x")

        entry = tk.Entry(
            frame,
            font=self.entry_font,
            show="*" if is_password else "",
            bd=1,
            relief="solid",
            bg="#ffffff"
        )
        entry.pack(fill="x", ipady=5, pady=(2, 10))

        setattr(self, f"{attr_name}_entry", entry)

    def validate_registration(self):
        u = self.user_entry.get()
        e = self.email_entry.get()
        p = self.pass_entry.get()
        c = self.confirm_entry.get()

        if not all([u, e, p, c]):
            messagebox.showwarning("Thông báo", "Vui lòng điền đầy đủ thông tin!")
            return

        if p != c:
            messagebox.showerror("Lỗi", "Mật khẩu xác nhận không khớp!")
            return

        messagebox.showinfo("Thành công", f"Chào mừng {u}!\nTài khoản đã được khởi tạo.")


def show():
    app = tk.Tk()
    ui = RegisterUI(app)
    app.mainloop()


if __name__ == "__main__":
    show()