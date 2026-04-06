
sinh_vien = {
    "sv1":{
    "name": "An",
    "phonenumber": "0901234567"
    },
    "sv2":{
        "name": "Bình",
        "phonenumber": "0912345678"
    },
    "sv3":{
        "name": "Cường",
        "phonenumber": "0923456789"
    }
}
#kiểm tra xem "Bình" có trong danh bạ không, nếu có thì in số điện thoại của Bình
if "Bình" in sinh_vien["sv2"]["name"]:
    print("Số điện thoại của Bình là: ", sinh_vien["sv2"]["phonenumber"])
else:
    print("Bình không có trong danh bạ")
#Xóa thông tin của "Cường" khỏi danh bạ
if "Cường" in sinh_vien["sv3"]["name"]:
    del sinh_vien["sv3"]
    print("Đã xóa thông tin của Cường khỏi danh bạ")
else:
    print("Cường không có trong danh bạ")
#In danh bạ sau khi cập nhật
print("Danh bạ sau khi cập nhật là: ",sinh_vien)
