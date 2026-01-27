dem_so_chan = 0
dem_so_le = 0

while True:
    n = int(input("Nhập số (nhập số để dừng): "))

    if n == 0:
        break

    if n % 2 == 0:
        dem_so_chan += 1
    else:
        dem_so_le += 1

print("Số lượng số chẵn:",dem_so_chan)
print("Số lượng số lẻ:", dem_so_le)
