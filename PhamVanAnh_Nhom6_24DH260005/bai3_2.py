chuoi = "c7349bc2 d65ca 92 65bf bc8343 6e5 e868"

def dem_khoang_trang(s):
    return s.count(" ")

def dem_chu_so_4(s):
    return s.count("4")

def thay_so(s):
    s = s.replace("0"," số 0 ")
    s = s.replace("1"," số 1 ")
    s = s.replace("2"," số 2 ")
    s = s.replace("3"," số 3 ")
    s = s.replace("4"," số 4 ")
    s = s.replace("5"," số 5 ")
    s = s.replace("6"," số 6 ")
    s = s.replace("7"," số 7 ")
    s = s.replace("8"," số 8 ")
    s = s.replace("9"," số 9 ")
    return s

print("Số lượng khoảng trắng trong chuỗi:", dem_khoang_trang(chuoi))
print("Số lượng chữ số 4 trong chuỗi:", dem_chu_so_4(chuoi))
print("Chuỗi sau khi thay thế số thành dạng chữ:", thay_so(chuoi))