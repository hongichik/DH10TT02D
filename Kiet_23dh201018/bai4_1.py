# --- BÀI TẬP 1: QUẢN LÝ DANH SÁCH TRÁI CÂY ---

# 1. Yêu cầu người dùng nhập 5 loại trái cây vào danh sách
print("Nhập vào 5 loại trái cây yêu thích của bạn:")
fruits = []
for i in range(5):
    item = input(f"Nhập loại trái cây thứ {i+1}: ")
    fruits.append(item)

# Xuất dòng gốc sau khi nhập xong
print("\n1. Danh sách gốc ban đầu:", fruits)

# 2. Nhập thêm một loại trái cây mới vào cuối danh sách
new_fruit = input("Nhập thêm một loại trái cây nữa để thêm vào cuối: ")
fruits.append(new_fruit)
print("2. Danh sách sau khi thêm mới:", fruits)

# 3. Thay đổi trái cây ở vị trí thứ 2 thành "Mango"
# Vị trí thứ 2 có index là 1 trong Python
if len(fruits) >= 2:
    fruits[1] = "Mango"
    print("3. Danh sách sau khi sửa vị trí thứ 2 thành 'Mango':", fruits)

# 4. Xóa trái cây ở vị trí cuối cùng
fruits.pop()
print("4. Danh sách sau khi xóa phần tử cuối cùng:", fruits)

