def khoitao(n):
    numbers = []
    for i in range(n):
        so = int(input(f"Nhap so nguyen thu {i + 1}: "))
        numbers.append(so)
    return numbers
def timmaxmin(numbers):
    min_val = max_val = numbers[0]
    for n in numbers:
        if n > max_val:
            max_val = n
        if n < min_val:
            min_val = n
    return max_val, min_val
def chuyenchuoi(numbers):
    return "-".join(map(str, numbers))
def main():
    ds_so = khoitao(4)
    cuc_dai, cuc_tieu= timmaxmin(ds_so)
    print(f"Gia tri lon nhat: {cuc_dai}")
    print(f"Gia tri nho nhat: {cuc_tieu}")
    chuoiketqua = chuyenchuoi(ds_so)
    print(f"Ket qua chuoi : {chuoiketqua}")
if __name__ == "__main__":
    main()
