"""
Bài 7: Đếm số chẵn - lẻ
Chức năng: Liên tục nhập số, dừng khi nhập 0, đếm số lượng số chẵn và số lẻ
"""


def count_even_odd() -> None:
    """
    Liên tục nhập số từ bàn phím.
    Dừng khi nhập 0.
    Đếm và in ra số lượng số chẵn và số lẻ.
    """
    even_count = 0
    odd_count = 0
    
    print("Liên tục nhập số (nhập 0 để dừng):")
    
    while True:
        try:
            num = int(input("Nhập số: "))
            
            if num == 0:
                break
            
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
                
        except ValueError:
            print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")
    
    # Hiển thị kết quả
    print("\n" + "=" * 30)
    print(f"Số lượng số chẵn: {even_count}")
    print(f"Số lượng số lẻ: {odd_count}")
    print("=" * 30)


if __name__ == "__main__":
    count_even_odd()