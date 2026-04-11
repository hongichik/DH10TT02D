def nhap():
    MaSV = input("Nhap ma sinh vien: ")
    ten = input("Nhap ten sinh vien: ")
    diem = float(input("Nhap diem sinh vien: "))
    return {"MaSV": MaSV, "ten": ten, "diem": diem}
def DTB(sinhvien_list):
    if not sinhvien_list:
        return 0
    tong_diem = sum(sv['diem'] for sv in sinhvien_list)
    return tong_diem / len(sinhvien_list)
def loc (sinhvien_list, diem = 5.0):
    danhsachloc = [sv for sv in sinhvien_list if sv['diem'] >= diem]
    return {"Danh sach sinh vien co diem lon hon hoac bang 5.0": danhsachloc}

danh_sach_sv = []
print("Nhap thong tin 3 sinh vien")
for i in range(3):
    print("Sinh vien: ", i+1)
    sv = nhap()
    danh_sach_sv.append(sv)
dtb_chung = DTB(danh_sach_sv)
print("Diem trung binh cua tat ca sinh vien: ", dtb_chung)

print("Danh sach sinh vien co diem lon hon hoac bang 7.0:")
sv_gioi = loc(danh_sach_sv,7.0)

if not sv_gioi:
    print("Khong co sinh vien gioi nao !")
else:
    print(f"- {sv['ten']} (MSV: {sv['MaSV']}) với {sv['diem']} điểm")