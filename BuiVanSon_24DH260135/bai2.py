sochan = 0
sole = 0

while True:
    num = int(input("Nhập số: "))
    
    if num == 0:
        print("Kết thúc chương trình.")
        break
    
    if num % 2 == 0:
        sochan += 1
    else:
        sole += 1

print("Số lượng số chẵn là :", sochan)
print("Số lượng số lẻ là :", sole)
