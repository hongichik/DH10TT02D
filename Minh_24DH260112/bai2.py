chan = 0
le = 0

while True:
    n = int(input("Nhap so (nhap so de dung): "))

    if num == 0:
        print("Ket thuc chuong trinh.")
        break

    if n % 2 == 0:
        dem_so_chan += 1
    else:
        dem_so_le += 1

print ("So luong so chan:, so chan")
print ("So luoong so le:, so le" )