N = int(input("Mời nhập số nguyên dương N: "))
i = 1
tong = 0

while i < N:
    if N % i == 0:
        tong += i
    i += 1
    
if tong == N:
    print("Số",N, "là số hoàn hảo")
else:
    print("Số",N, "không phải là số hoàn hảo")