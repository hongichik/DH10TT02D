# Tạo danh bạ điện thoại
phonebook = {
    "An": "0901234567",
    "Binh": "0912345678",
    "Cuong": "0923456789"
}

print("Danh bạ ban đầu:", phonebook)

# Kiểm tra Binh có trong danh bạ không
if "Binh" in phonebook:
    print("Số điện thoại của Binh:", phonebook["Binh"])
else:
    print("Không tìm thấy Binh")

# Xóa thông tin của Cuong
if "Cuong" in phonebook:
    del phonebook["Cuong"]

# In danh bạ sau khi cập nhật
print("Danh bạ sau khi cập nhật:", phonebook)