danh_ba = {
    "An": "0901234567",
    "Bình": "0912345678",
    "Cường": "0923456789"
}

if "Bình" in danh_ba:
    print(f"Số điện thoại của Bình là: {danh_ba['Bình']}")
else:
    print("Không tìm thấy Bình trong danh bạ.")

if "Cường" in danh_ba:
    del danh_ba["Cường"]

print("Danh bạ sau khi cập nhật:")
print(danh_ba)