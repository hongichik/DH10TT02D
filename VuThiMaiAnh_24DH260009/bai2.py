dem_chan = 0
dem_le = 0

while True:
    n = int(input("Nhập số (nhập 0 để dừng): "))
    if n == 0:
        break
    if n % 2 == 0:
        dem_chan += 1
    else:
        dem_le += 1

print("Số lượng số chẵn:", dem_chan)
print("Số lượng số lẻ:", dem_le)