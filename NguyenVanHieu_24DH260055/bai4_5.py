
kho={"apple": 50,
     "banana": 30,
     "orange": 20}
#Giảm số lượng "banana" xuống còn 20
kho["banana"]-=10
#Thêm sản phẩm "grape" với số lượng 15
kho["grape"]=15
#Tính và in tổng số lượng tất cả các sản phẩm trong kho
tonh_so_luong= sum(kho.values())
print("Thông tin kho: ", kho)
print("Tổng số lượng tất cả các sản phẩm trong kho:", tonh_so_luong)
