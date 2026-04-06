import tkinter as tk
from tkinter import messagebox

reg = tk.Tk()
reg.title("Tạo tài khoản")
reg.geometry("380x420")
reg.resizable(False, False)
reg.configure(bg="#f5e8d3")

# Tiêu đề
tk.Label(reg, text="TẠO TÀI KHOẢN", font=("Arial", 18, "bold"), bg="#f5e8d3").pack(pady=25)

# Tên đăng nhập
tk.Label(reg, text="Tên đăng nhập:", font=("Arial", 10), bg="#f5e8d3").place(x=50, y=90)
entry_user = tk.Entry(reg, font=("Arial", 11), width=25)
entry_user.place(x=170, y=90)

# Mật khẩu
tk.Label(reg, text="Mật khẩu:", font=("Arial", 10), bg="#f5e8d3").place(x=50, y=130)
entry_pass = tk.Entry(reg, show="*", font=("Arial", 11), width=25)
entry_pass.place(x=170, y=130)

# Xác nhận mật khẩu
tk.Label(reg, text="Xác nhận mật khẩu:", font=("Arial", 10), bg="#f5e8d3").place(x=50, y=170)
entry_confirm = tk.Entry(reg, show="*", font=("Arial", 11), width=25)
entry_confirm.place(x=170, y=170)

# Email 
tk.Label(reg, text="Email:", font=("Arial", 10), bg="#f5e8d3").place(x=50, y=210)
entry_email = tk.Entry(reg, font=("Arial", 11), width=25)
entry_email.place(x=170, y=210)

# Hàm đăng ký
def register():
    user = entry_user.get()
    pas = entry_pass.get()
    confirm = entry_confirm.get()
    email = entry_email.get()

    if not all([user, pas, confirm, email]):
        messagebox.showwarning("Thông báo", "Vui lòng điền đầy đủ thông tin!")
        return

    if pas != confirm:
        messagebox.showerror("Lỗi", "Mật khẩu xác nhận không khớp!")
        return

    messagebox.showinfo("Thành công", 
                      f"Tài khoản '{user}' đã được tạo thành công!\n"
                      f"Email: {email}")

# Nút Tạo tài khoản
tk.Button(reg, text="TẠO TÀI KHOẢN", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white",
          width=20, command=register).place(x=90, y=270)

# Chữ dưới cùng
tk.Label(reg, text="Đã có tài khoản? Đăng nhập ngay", 
         font=("Arial", 9), fg="#007bff", bg="#f5e8d3").place(x=95, y=330)

reg.mainloop()