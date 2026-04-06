# a. Hàm khởi tạo danh sách số
def khoitao(n):
    danhsach = []
    for i in range(n):
        x = int(input(f"Nhập số thứ {i+1}: "))
        danhsach.append(x)
    return danhsach


# b. Hàm tìm max và min
def timmaxmin(numbers):
    if len(numbers) == 0:
        return (None, None)
    
    max_val = numbers[0]
    min_val = numbers[0]
    
    for x in numbers:
        if x > max_val:
            max_val = x
        if x < min_val:
            min_val = x
            
    return (max_val, min_val)


# c. Hàm chuyển danh sách thành chuỗi
def chuyenchuoi(numbers):
    chuoi = "-".join(str(x) for x in numbers)
    return chuoi


# d. Chương trình chính
danhsach = khoitao(4)

max_val, min_val = timmaxmin(danhsach)
print("Giá trị lớn nhất:", max_val)
print("Giá trị nhỏ nhất:", min_val)

chuoi = chuyenchuoi(danhsach)
print("Chuỗi sau khi chuyển:", chuoi)
