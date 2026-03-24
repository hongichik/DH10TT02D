ds1 =[2,4,6,8,10]
ds2 =[1,3,5,7,9]
print(ds1)
print(ds2)

ds3= ds1 + ds2
print("ghép 2 danh sách thành 1 danh sách mới:",ds3)

for i in range (len(ds3)):
    ds3[i]= ds3[i]*2
print("nhân đôi các phần tử trong danh sách mới",ds3)
