kho = {
    "apple": 50,
    "banana": 30,
    "orange": 20
}

print("Kho ban đầu:", kho)
kho["banana"] = 10
print("Sau khi giảm banana:", kho)
kho["grape"] = 15
print("Sau khi thêm grape:", kho)
tong = sum(kho.values())
print("Tổng số lượng:", tong)