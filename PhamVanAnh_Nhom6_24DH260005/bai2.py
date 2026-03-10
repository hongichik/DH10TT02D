chan = 0
le = 0

while True:
    n = int(input("Nhập số nguyên dương (Nhập 0 để dừng): "))
    
    if n == 0:
        print("Kết thúc chương trình.")
        break
    elif n % 2 == 0:
        chan += 1
    else:
        le += 1

print("Số lượng số chẵn:", chan)
print("Số lượng số lẻ:", le)