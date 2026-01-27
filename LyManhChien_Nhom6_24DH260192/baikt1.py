n = int(input("Nhap so nguyen N: "))

if n <= 0:
    print("Vui long nhap so nguyen duong.")
else:
    tong = 0

    for i in range(1, n):
        if n % i == 0:
            tong += i

    if tong == n:
        print(n, "la so hoan hao.")
    else:
        print(n, "khong phai la so hoan hao.")