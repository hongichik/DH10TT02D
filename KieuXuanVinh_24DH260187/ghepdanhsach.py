list1 = [1, 2, 3]
list2 = [4, 5, 6]

print(list1, list2)

list3 = list1 + list2
print("Sau khi ghep:", list3)

for i in range(len(list3)):
    list3[i] = list3[i] * 2

print("Sau khi nhan doi:", list3)