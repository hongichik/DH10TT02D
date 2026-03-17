# Chuỗi ban đầu
s = "c734 9bc2 d65ca 92 65bf bc8343 6e5 e868"


# 1. Hàm đếm số khoảng trắng
def dem_khoang_trang(chuoi):
    dem = 0
    for ky_tu in chuoi:
        if ky_tu == " ":   # nếu ký tự là khoảng trắng
            dem += 1
    return dem


# 2. Hàm đếm số lần xuất hiện của số 4
def dem_so_4(chuoi):
    dem = 0
    for ky_tu in chuoi:
        if ky_tu == "4":   # nếu ký tự là số 4
            dem += 1
    return dem


# 3. Hàm thay thế tất cả chữ số thành dạng chữ "số x"
def thay_the_so(chuoi):
    ket_qua = ""

    for ky_tu in chuoi:
        if ky_tu.isdigit():     # kiểm tra ký tự có phải là chữ số không
            ket_qua += "số " + ky_tu
        else:
            ket_qua += ky_tu

    return ket_qua


# Gọi các hàm
print("Số khoảng trắng:", dem_khoang_trang(s))
print("Số lần xuất hiện của số 4:", dem_so_4(s))
print("Chuỗi sau khi thay thế:", thay_the_so(s))