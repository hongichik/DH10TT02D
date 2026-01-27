while True:
    so = int(input("Nhập số nguyên dương n: "))
    if so == 0:
        print("Kết thúc chương trình.")
        break
    if so %2 == 0:
        print(f"{so} là số chẵn.")
    else:
        print(f"{so} là số lẻ.")