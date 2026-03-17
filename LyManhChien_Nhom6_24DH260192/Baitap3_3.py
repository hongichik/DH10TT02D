# Chuỗi ban đầu
s = "c734 9bc2 d65ca 92 65bf bc8343 6e5 e868"

# 1. Hàm đếm số lượng khoảng trắng
def dem_khoang_trang(chuoi):
    dem = 0
    for i in chuoi:
        if i == " ":
            dem += 1
    return dem


# 2. Hàm đếm số lượng chữ số 4
def dem_so_4(chuoi):
    dem = 0
    for i in chuoi:
        if i == "4":
            dem += 1
    return dem


# 3. Hàm thay thế chữ số thành dạng chữ
def thay_the_so(chuoi):
    ket_qua = ""
    for i in chuoi:
        if i.isdigit():           # kiểm tra có phải số không
            ket_qua += "số " + i
        else:
            ket_qua += i
    return ket_qua


# Gọi các hàm
print("Số khoảng trắng:", dem_khoang_trang(s))
print("Số chữ số 4:", dem_so_4(s))
print("Chuỗi sau khi thay thế:")
print(thay_the_so(s))