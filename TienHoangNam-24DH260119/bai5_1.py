def nhap_so(n):
    danh_sach = []
    for i in range(n):
        # Truy xuất giá trị thứ i+1 từ người dùng
        so = int(input(f"Nhập số nguyên thứ {i + 1}: "))
        danh_sach.append(so)
    return danh_sach


def thong_ke_so(ds):
    if not ds:  # Case: Danh sách rỗng
        return (0, None)

    # List comprehension lọc số chẵn và hàm built-in tìm max
    so_chan = len([x for x in ds if x % 2 == 0])
    gia_tri_max = max(ds)

    return (so_chan, gia_tri_max)
def chuyen_set(ds):
    # Chuyển đổi kiểu dữ liệu trực tiếp
    return set(ds)


def main():
    # 1. Khởi tạo dữ liệu (n=5)
    print("--- Bước 1: Nhập dữ liệu ---")
    danh_sach = nhap_so(5)

    # 2. Thống kê dữ liệu
    # Unpack tuple trả về từ hàm thong_ke_so
    count_chan, max_val = thong_ke_so(danh_sach)
    print("\n--- Bước 2: Thống kê ---")
    print(f"Số lượng số chẵn: {count_chan}")
    print(f"Giá trị lớn nhất: {max_val}")

    # 3. Chuyển đổi cấu trúc dữ liệu
    tap_hop = chuyen_set(danh_sach)
    print("\n--- Bước 3: Chuyển sang Set ---")
    print(f"Tập hợp (loại trùng): {tap_hop}")


if __name__ == "__main__":
    main()