demchan = 0
demle = 0

while True:
    n = int(input("Nhập số (nhập 0 để dừng): "))

    if n == 0:
        print("Kết thúc chương trình!")
        break

    if n % 2 == 0:
        print(f"Số {n} là số chẵn")
        demchan += 1
        print(f"Số {n} là số số lẻ")
        demle += 1
        
print("Số lượng số chẵn là :", demchan)
print("Số lượng số lẻ là :", demle)