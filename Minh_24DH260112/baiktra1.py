N = int(input("Nhập số nguyên N: "))
tong = 0
for i in range(1, N):
    if N % i == 0:     
        tong = tong + i
if tong == N:
    print(N, "là số hoàn hảo.")
else:
    print(N, "không phải là số hoàn hảo.")
