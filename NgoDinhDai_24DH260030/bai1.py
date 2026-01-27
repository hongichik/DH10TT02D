ds = []

while True:
    n = int(input("Nhập số (0 để dừng): "))
    if n == 0:
        break
    ds.append(n)

dem_chan = 0
dem_le = 0

for x in ds:
    if x % 2 == 0:
        dem_chan += 1
    else:
        dem_le += 1

print("Số lượng số chẵn:", dem_chan)
print("Số lượng số lẻ:", dem_le)
