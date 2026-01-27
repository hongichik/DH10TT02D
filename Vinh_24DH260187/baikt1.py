n = int(input("Mời nhập số nguyên: "))
TongUoc = 0
for i in range(1, n ):
    if i % 2 == 0:
        TongUoc += i
if TongUoc == n:
    print(f"số {n} là số hoàn hảo")
else:
    print(f"số {n} không phải là số hoàn hảo")