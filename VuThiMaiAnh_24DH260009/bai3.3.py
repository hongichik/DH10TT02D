
s = "c734 9bc2 d65ca 92 65bf bc8343 6e5 e868"

def dem_khoang_trang(chuoi):
    count = 0
    for c in chuoi:
        if c == " ":
            count += 1
    return count

def dem_so_4(chuoi):
    count = 0
    for c in chuoi:
        if c == "4":
            count += 1
    return count

def thay_so_bang_chu(chuoi):
    ket_qua = ""
    for c in chuoi:
        if c.isdigit():
            ket_qua += "số " + c
        else:
            ket_qua += c
    return ket_qua

print("Số khoảng trắng:", dem_khoang_trang(s))
print("Số lượng số 4:", dem_so_4(s))
print("Chuỗi sau khi thay:", thay_so_bang_chu(s))