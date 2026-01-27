a=int(input("Nhap so: "))
t=0
for i in range(1,a):
    if a%i==0:
        t+=i
if t==a:
    print(a, "la so hoan hao")
else:
    print(a, "khong la so hoan hao")