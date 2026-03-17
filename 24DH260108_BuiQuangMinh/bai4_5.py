kho ={
    "apple": 50,
    "banana": 30,
    "orange": 20

}
print(kho)

kho["banana"] = kho["banana"] -10
print("Giảm số lượng 'banana' xuống 10: ",kho)

kho["grape"] = 15
print("Thêm sản phẩm 'grape' với số lượng 15: ",kho)

tong = sum(kho.values())
print("Tổng số lượng tất cả các sản phẩm trong kho: ",tong)
