# Tạo dictionary chứa thông tin cá nhân
Tu_dien = {
    "ten": "Chiến",
    "tuoi": 20,
    "nghe_nghiep": "Sinh vien"
}
print(Tu_dien)
print(Tu_dien)
# Thêm thông tin email
Tu_dien["email"] = "chien@gmail.com"

# Sửa tuổi thành 25
Tu_dien["tuoi"] = 25

# Xóa thông tin nghề nghiệp
del Tu_dien["nghe_nghiep"]

# In dictionary
print("Thông tin cá nhân:", Tu_dien)