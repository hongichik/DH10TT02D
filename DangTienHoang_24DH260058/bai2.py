while True:
    so = int(input("Nhap so nguyen dem so chan"))
    if so == 0:
        print("Ket thuc chuong trinh")
        break
    if so %2 == 0:
        print(f"{so}la so chan")
    else:
        print(f"{so}la so le")    