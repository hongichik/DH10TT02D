kho = {"apple": 50, "banana" :30, "orange":20}
print("Số sản phẩm trong kho: ",kho)
kho["banana"]= 10
print("Số lượng banana giảm xuống 10: ",kho)
kho["grape"]= 15
print("Thêm grape vào kho: ",kho)
kho = sum(kho.values())
print("Tổng số sản phẩm trong kho là: ",kho)