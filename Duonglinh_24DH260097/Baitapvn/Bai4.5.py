#Quảng Lý kho
#Tạo Kho
Kho = {
    "apple": 50,
    "banana": 30,
    "orange": 20
}

#Giảm banana xuống 10
Kho["banana"] = 10

#Thêm Grape
Kho["grape"] = 15

#Tính Tổng
tong = 0

for value in Kho.values():
    tong += value

print("Tổng:", tong)
