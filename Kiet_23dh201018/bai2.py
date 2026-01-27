while True:
    s0 = int(input("Nhap so : "))

    if s0 == 0:
        print("ket thuc chuong trinh")
        break

    if 'chan' not in locals():
        chan = 0
        le = 0

    if s0 % 2 == 0:
        chan = chan + 1

    else:
        le = le + 1



print("--- TONG KET ---")
print("So luong so chan la:", chan)
print("So luong so le la:", le)

