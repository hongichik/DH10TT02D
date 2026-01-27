
n = int(input("Nhập số nguyên N: "))

# Biến lưu tổng các ước của N
tong = 0
for i in range(1, n):
    # Nếu i là ước của N
    if n % i == 0:
        tong += i  # Cộng i vào tổng các ước

# Kiểm tra số hoàn hảo
if tong == n:
    print(n, "là số hoàn hảo")
else:
    print(n, "không phải là số hoàn hảo")
