n = int (input ("Nhap so nguyen N: "))
tong = 0
for i in range(1 ,n):
    if n % i == 0:
        tong +=i
if tong == n and n >0:
    print(f"{n} la so hoan hao")
else:
    print(f"{n} la so khong hoan hao")