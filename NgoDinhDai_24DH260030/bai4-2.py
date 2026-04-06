list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("List 1:", list1)
print("List 2:", list2)
list3 = list1 + list2
print("Sau khi ghép:", list3)
list4 = []

for i in list3:
    list4.append(i * 2)

print("Sau khi nhân đôi:", list4)