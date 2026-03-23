kho = {
    "apple": 50,
    "banana": 30,
    "orange": 20
}

kho["banana"] = 10

kho["grape"] = 15

tong_so_luong = sum(kho.values())

print(f"Kho hàng hiện tại: {kho}")
print(f"Tổng số lượng sản phẩm trong kho: {tong_so_luong}")