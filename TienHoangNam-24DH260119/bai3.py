a = int(input("nhap so:"))
tong = 0;
for i in range(1, a):
    if(a%i==0):
        tong += i
if tong == a:
    print(a,"Là so hoàn hảo")
else:
    print(a,"Khong la số hoàn hảo")
