# phần a
def nhap():
    masv = input("Nhập MaSV: ")
    ten = input("Nhập tên sinh viên: ")
    diem = float(input("Nhập điểm: "))
    return {"MaSV": masv, "ten": ten, "diem": diem}

#phần b
def DTB(sinhvien_list):
    if not sinhvien_list:
        return 0
    
    tong_diem = sum(sv["diem"] for sv in sinhvien_list)
    return tong_diem / len(sinhvien_list)

#phần c
def loc(sinhvien_list, diem_nguong=5.0):
    danh_sach_loc = [sv for sv in sinhvien_list if sv["diem"] >= diem_nguong]
    return danh_sach_loc

#phần d
if __name__ == "__main__":
    danh_sach_sv = []
    
    print("--- Nhập thông tin 3 sinh viên ---")
    for i in range(3):
        print(f"Sinh viên thứ {i+1}:")
        sv = nhap()
        danh_sach_sv.append(sv)
    

    trung_binh = DTB(danh_sach_sv)
    print(f"\nĐiểm trung bình của tất cả sinh viên: {trung_binh:.2f}")

    print("\n--- Danh sách sinh viên có điểm >= 7.0 ---")
    danh_sach_dat = loc(danh_sach_sv, 7.0)
    
    if not danh_sach_dat:
        print("Không có sinh viên nào đạt mức điểm này.")
    else:
        for sv in danh_sach_dat:
            print(f"MaSV: {sv['MaSV']}, Tên: {sv['ten']}, Điểm: {sv['diem']}")
