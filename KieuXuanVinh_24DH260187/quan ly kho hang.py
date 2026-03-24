kho = {
    "apple": 50,
    "banana": 30,   
    "orange": 20
}
print("Kho hàng ban đầu:", kho)
kho["banana"] = kho["banana"] - 20
print("Kho hàng sau khi giảm số lượng quả chuối:", kho)
kho["grape"] = 15
print("Kho hàng sau khi thêm nho:", kho)
tong = sum(kho.values())
print("Tổng số lượng hàng hóa trong kho:", tong)