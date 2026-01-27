tong =0
while True:
    n = int(input("Nhập số nguyên: "))
    if n > 0:
        break
for i in range(1, n - 1):
    if n%i ==0:
        tong += i
if tong ==n:
    print(n,"là số hoàn hảo")
else:
    print(n,"không phải là số hoàn hảo")