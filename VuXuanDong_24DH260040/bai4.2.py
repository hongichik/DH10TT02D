thong_tin ={
    "tên": "Vu Xuan Dong",
    "tuổi": 20,
    "nghề nghiệp": "Sinh viên"
}
print(thong_tin)

thong_tin["email"]= "dongvu2903@gmail.com"
thong_tin["tuổi"]=25
print("Thông tin sau khi thêm email và sửa tuổi:",thong_tin)

del thong_tin["nghề nghiệp"]
print("Thông tin cá nhân sau khi cập nhật:",thong_tin)
