def nhap_so(n):
    danh_sach =[]
    for i in range(n):
        print("Nhap so thu",i+1,":", end="")
        so = input("")
        danh_sach .append(so)
    return danh_sach

print("Nhap so luong so: ", end="")
n =int(input(""))
ds = nhap_so(n)
print("Danh sach so vua nhap: ", ds)

def thongkeso (danhsach):
    sochan = 0
    max = 0
    for i in danhsach:
        print(i)
        if i > max:
            max = i
        if i % 2 == 0:
            sochan += 1
        return sochan, max

sochan, max = thongkeso(ds)
print("So luong so chan: ", sochan)
print("So lon nhat", max)

def chuyen_set(danhsach):
    for i in danhsach:
        for j in danhsach:
            if i == j:
                danhsach.remove(j)
    return danhsach

print("Danh sach sau khi chuyen sang set: ", chuyen_set(ds))