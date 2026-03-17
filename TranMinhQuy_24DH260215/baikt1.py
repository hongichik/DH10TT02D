N = int(input("Nhập số nguyên N: "))
tong_uoc = 0
for i in range(1, N):
    if N % i == 0:
        tong_uoc += i
if tong_uoc == N:
    print(N, "là số hoàn hảo")
else:
    print(N, "không phải là số hoàn hảo")