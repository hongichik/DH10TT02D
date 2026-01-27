chan = 0
le = 0
print("Nhap vao cac so nguyen")
while True:
    a = int(input("Nhap so:"))
    if a == 0:
        print("Ket thuc chuong trinh")
        break
    if a % 2 == 0:
        chan += 1
    else:
        le += 1
print(f"So luong chan: {chan}")
print(f"So luong le: {le}")