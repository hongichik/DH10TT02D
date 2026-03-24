# tạo dictionary để điền thông tin sinh viên
student = {
    "id": "SV001",
    "ten": "An",
    "gpa": 8.5,
    "age": 20   
}

# Thêm ngành
student["majob"] = "CNTT"

#tăng điểm
student["gpa"] += 0.5

#in tất cả
for key, value in student.items():
    print(key,":",value)