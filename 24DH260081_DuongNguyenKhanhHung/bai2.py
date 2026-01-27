sochan=0
sole=0
while True:
    n=int(input("Moi nhap so n(nhap 0 de dung lai)"))
    if n==0:
        break
    if n%2==0:
        sochan +=1
    else:
        sole +=1
print("So chan la: ", sochan)
print("So le la: ",sole)