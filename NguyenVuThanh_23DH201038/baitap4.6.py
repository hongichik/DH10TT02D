danh_ba = {
    "Uyên": "0358359104",
    "Bình": "0912345678",
    "Kiệt": "0923456789"
}

if "Bình" in danh_ba:
    print(f"Số điện thoại của Bình là: {danh_ba['Bình']}")
else:
    print("Không tìm thấy Bình trong danh bạ.")

# 3. Xóa thông tin của "Cường" khỏi danh bạ
# Cách 1: Sử dụng lệnh del
if "Kiệt" in danh_ba:
    del danh_ba["Kiệt"]

print("\nDanh bạ sau khi cập nhật:")
print(danh_ba)