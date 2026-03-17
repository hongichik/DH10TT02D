#dictionary
#Tao thong tin ca nhan
thong_tin={"ten":"Nguyễn Đức Trường",
           "tuoi":22,
           "nghe_nghiep":"sinh viên"
           }

thong_tin["email"]="ductruong6116@gmail.com"
print("Thêm thông tin email:", thong_tin)
thong_tin["tuoi"]=25
print("Sửa tuổi thành 25: ", thong_tin)
del thong_tin["nghe_nghiep"]
print("Xóa thông tin nghề nghiệp:", thong_tin)