chan = 0
le = 0

while True:
    n = int(input ("Nhap so(0 để dừng): "))
    if n==0:
        break
    if n % 2 == 0:
        chan += 1
    else:
        le += 1
print(f"Số lượng số chẵn: {chan}")
print(f"Số lượng số lẻ: {le}")