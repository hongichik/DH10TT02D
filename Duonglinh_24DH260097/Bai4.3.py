# Tạo List
list1 = [ 1, 2, 3]
list2 = [ 4, 5, 6]

#ghép list
list3 = list1 + list2

result = []#result ten biến , mục đích nó là danh sách rỗng

for x in list3:# duyệt từng phần tử trong list3, gán vào biến x.
    result.append(x*2)

#In ra
print("danh sách sau khi xử lý:", result)