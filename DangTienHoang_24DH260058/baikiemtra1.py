n = int(input("Nhap so nguyen duong N: "))

tong = 0

for i in range(1, n):
    if n % i == 0:
        tong += i

if tong == n:
    print(n, "la so hoan hao")
else:
    print(n, "khong phai la so hoan hao")
