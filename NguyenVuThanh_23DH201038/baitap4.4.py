sinh_vien = {
    "id": "23DH201038",
    "name": "Thanh",
    "age": 20,
    "gpa": 8.5
}

sinh_vien["major"] = "CNTT"

sinh_vien["gpa"] += 0.5

print("--- Thông tin sinh viên ---")
for key, value in sinh_vien.items():
    print(f"{key}: {value}")