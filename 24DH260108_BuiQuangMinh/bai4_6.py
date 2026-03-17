danh_ba ={
    "Nam New": "0987654321",
    "Quý Béo": "0123123123",
    "A Lĩnh Ciute": "08686868686"

}
print("Danh bạ: ",danh_ba)

if "A Lĩnh Ciute" in danh_ba:
    print(f"Số điện thoại của A Lĩnh Ciute là: {danh_ba['A Lĩnh Ciute']}")
else:
    print("Không tìm thấy tên A Lĩnh Ciute trong danh bạ!")

if "Quý Béo" in danh_ba:
    del danh_ba["Quý Béo"]
print("Danh bạ sau khi cập nhật: ",danh_ba)
