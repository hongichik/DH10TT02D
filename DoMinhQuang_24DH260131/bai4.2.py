#dictionary
#Tao thong tin ca nhan
thong_tin={"ten":"Do Minh Quang",
           "tuoi":19,
           "nghe_nghiep":"sinh viên"
           }

thong_tin["email"]="qdo72877@gmail.com"
print("Thêm thông tin email:", thong_tin)
thong_tin["tuoi"]=25
print("Sửa tuổi thành 25: ", thong_tin)
del thong_tin["nghe_nghiep"]
print("Xóa thông tin nghề nghiệp:", thong_tin)