def khoitao(n):
    numbers = []
    for i in range(n):
        so = int(input(f"Nhập số nguyên thứ {i + 1}: "))
        numbers.append(so)
    return numbers

def timmaxmin(numbers):
    if not numbers:
        return (None, None)
    max_val = min_val = numbers[0]

    for num in numbers:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    return (max_val, min_val)
def chuyenchuoi(numbers):
    return "-".join(map(str, numbers))
def main():
    ds_so = khoitao(4)

    cuc_dai, cuc_tieu = timmaxmin(ds_so)
    print(f"\nGiá trị lớn nhất: {cuc_dai}")
    print(f"Giá trị nhỏ nhất: {cuc_tieu}")

    chuoi_ket_qua = chuyenchuoi(ds_so)
    print(f"Chuỗi kết quả: {chuoi_ket_qua}")


if __name__ == "__main__":
    main()