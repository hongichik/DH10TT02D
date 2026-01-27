count_even = 0
count_odd = 0
print("nhâp các số nguyên (nhập 0 để dừng):")
while True:
    try:
        n = int(input("Số tiếp theo"))
        if  n == 0:
            break
        if n % 2 == 0:
            count_even += 1
        else :
            count_odd += 1
    except ValueError:
        print("Vui lòng chỉ nhập số nguyên!")
print("_"* 20)
print(f"Số lượng số chẵn: {count_even}")
print(f"Số lượng số lẻ  : {count_odd}")