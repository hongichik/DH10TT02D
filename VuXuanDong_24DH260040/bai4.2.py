tu_dien ={
    "tên": "Vu Xuan Dong",
    "tuổi": 20,
    "nghề nghiệp": "Sinh viên"
}
print(tu_dien)

tu_dien["email"]= "dongvu2903@gmail.com"
tu_dien["tuổi"]=25
print("Thông tin sau khi thêm email và sửa tuổi:",tu_dien)

del tu_dien["nghề nghiệp"]
print("Thông tin cá nhân sau khi cập nhật:",tu_dien)
