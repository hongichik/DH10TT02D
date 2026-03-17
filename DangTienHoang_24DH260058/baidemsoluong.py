def count_spaces(text):
    """Đếm số lượng dấu cách (space) trong chuỗi."""
    return text.count(" ")


def count_digit_four(text):
    """Đếm số lượng chữ số 4 xuất hiện trong chuỗi."""
    return text.count("4")


def replace_digits_with_words(text):
    """Thay tất cả chữ số 0-9 thành dạng chữ: 'số x'."""
    replacements = {
        "0": "số 0",
        "1": "số 1",
        "2": "số 2",
        "3": "số 3",
        "4": "số 4",
        "5": "số 5",
        "6": "số 6",
        "7": "số 7",
        "8": "số 8",
        "9": "số 9",
    }

    result = ""
    for char in text:
        if char in replacements:
            result += replacements[char]
        else:
            result += char
    return result


input_str = "c734 9bc2 d65ca 92 65bf bc8343 6e5 e868"

print("Chuỗi gốc:", input_str)
print("1. Số lượng khoảng trắng:", count_spaces(input_str))
print("2. Số lượng chữ số 4:", count_digit_four(input_str))
print("3. Chuỗi sau khi thay thế số:")
print(replace_digits_with_words(input_str))