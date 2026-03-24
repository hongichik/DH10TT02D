ds1 = [1, 2, 3]
ds2 = [4, 5, 6]

ds3 = ds1 + ds2
print(ds3)

for i in range(len(ds3)):
  ds3[i] = ds3[i] * 2
print(ds3)