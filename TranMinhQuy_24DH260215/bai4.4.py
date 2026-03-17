student = {
    "id": "24DH260215",
    "name": "Quy",
    "age": 19,
    "gpa": 9.0
}
student["major"] = "CNTT"
student["gpa"] += 0.5
for key, value in student.items():
    print(key, ":", value)
