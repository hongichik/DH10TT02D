demchan = 0
demle = 0

while True:
    n = int(input("Nhập số (Nhập 0 để dừng): "))

    if n == 0:
        print("Kết thúc chương trình")
        break
    if n % 2 == 0:
        demchan += 1
    else:
        demle += 1
print("số lượng số chẵn là:", demchan)
print("số lượng số lẻ là:", demle)