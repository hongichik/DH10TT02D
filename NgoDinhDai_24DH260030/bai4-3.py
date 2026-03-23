student = {
    "id": "SV001",
    "name": "An",
    "age": 20,
    "gpa": 8.5
}

print("Ban đầu:", student)
student["nghanh"] = "CNTT"
print("Sau khi thêm nghanh :", student)
student["gpa"] = student["gpa"] + 0.5
print("Sau khi tăng GPA:", student)



for key, value in student.items():
    print( "|",key, ":", value,"|")