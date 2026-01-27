n = int(input("Nhập số nguyên N: "))
tong_cac_uoc = 0
for i in range(1, n):
    if n % i == 0:
        tong_cac_uoc += i
if tong_cac_uoc == n:
    print(n, "là số hoàn hảo")
else:
    print(n, "không phải là số hoàn hảo")