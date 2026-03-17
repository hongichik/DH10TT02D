def dem_khoang_trang(s):
    dem = 0
    for i in s:
        if i == " ":
            dem = dem + 1
    return dem


def dem_so_4(s):
    dem = 0
    for i in s:
        if i == "4":
            dem = dem + 1
    return dem


def thay_so(s):
    ket_qua = ""

    for i in s:
        if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9":
            ket_qua = ket_qua + "số " + i
        else:
            ket_qua = ket_qua + i

    return ket_qua


s = "c734 9bc2 d65ca 92 65bf bc8343 6e5 e868"

print("Số khoảng trắng:", dem_khoang_trang(s))
print("Số lượng số 4:", dem_so_4(s))
print("Chuỗi sau khi thay:", thay_so(s))