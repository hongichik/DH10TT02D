n = int(input("Nhap chieu cao tam giac: "))

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))