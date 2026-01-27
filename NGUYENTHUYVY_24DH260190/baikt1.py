N = int(input("Nhập số nguyên n:"))
tong_uoc = 0
for i in range(1,N):
    if N% i==0:
        tong_uoc += i
    if tong_uoc == N and N >0:
        print(N, "la so hoan hao")
    else:
        print(N, "khong phai la so hoan hao")