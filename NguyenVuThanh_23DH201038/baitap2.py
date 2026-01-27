so_chan = 0
so_le = 0

while True:
    n = int(input("Nhập số (nhập 0 để dừng): "))

    if n == 0:
        break

    if n % 2 == 0:
        so_chan += 1
    else:
        so_le += 1

print("-" * 20)
print(f"Số lượng số chẵn: {so_chan}")
print(f"Số lượng số lẻ: {so_le}")
