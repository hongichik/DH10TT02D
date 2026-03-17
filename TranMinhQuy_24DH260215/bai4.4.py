# Tạo dictionary thông tin sinh viên
student = {
    "id": "24DH260215",
    "name": "Quy",
    "age": 19,
    "gpa": 9.0
}

# Thêm ngành học
student["major"] = "CNTT"

# Tăng điểm trung bình thêm 0.5
student["gpa"] += 0.5

# In tất cả key và value
for key, value in student.items():
    print(key, ":", value)
