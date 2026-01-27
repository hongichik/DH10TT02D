sochan = 0
sole = 0

while True:
    so = int(input("Nhập số nguyên dương n: "))
    if so == 0:
        print("Kết thúc chương trình.")
        break
    if so %2 == 0:
        sochan += 1
    else:
        print(f"{so} là số lẻ.")
        sole += 1
print(f"Tổng số chẵn đã nhập: {sochan}")
print(f"Tổng số lẻ đã nhập: {sole}")