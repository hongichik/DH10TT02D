i=0
d=0
while True:
    a=int(input("Nhap so: "))
    if a==0:
        break
    if a%2==0:
        i+=1
    else:
        d+=1
print("tong so chan:",i)
print("tong so le:",d)