def nhap():
    masv = input("Nhap ma SV: ")
    ten = input("Nhap ten SV: ")
    diem = float(input("Nhap diem: "))
    
    return {"MaSV": masv, "ten": ten, "diem": diem}

def DTB(sinhvien):
    if len(sinhvien) == 0:
        return 0
    
    tong = 0
    for sv in sinhvien:
        tong += sv["diem"]
    
    return tong / len(sinhvien)

def loc(sinhvien, diem=5.0):
    ketqua = []
    for sv in sinhvien:
        if sv["diem"] >= diem:
            ketqua.append(sv)
    return ketqua

def main():
    danh_sach = []

    print("====== Nhap thong tin 3 sinh vien =====")
    for i in range(3):
        print(f"\nSinh vien {i+1}:")
        sv = nhap()
        danh_sach.append(sv)

    dtb = DTB(danh_sach)
    print("\nDiem trung binh:", dtb)

    ds_loc = loc(danh_sach, 7.0)
    
    print("\nDanh sach sinh vien co diem >= 7:")
    for sv in ds_loc:
        print(sv)

main()