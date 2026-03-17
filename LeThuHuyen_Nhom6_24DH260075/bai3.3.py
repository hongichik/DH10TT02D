s = "c734 9bc2 d65ca 92 65bf bc8343 6e5 e868"

def dem_khoang_trang(chuoi):
    return chuoi.count(" ")

def dem_so_4(chuoi):
    return chuoi.count("4")

def thay_so(chuoi):
    ketqua = ""
    for i in chuoi:
        if i.isdigit():
            ketqua += "số " + i
        else:
            ketqua += i
    return ketqua

print("Số khoảng trắng:", dem_khoang_trang(s))
print("Số chữ số 4:", dem_so_4(s))
print("Chuỗi sau khi thay:", thay_so(s))