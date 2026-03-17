
print("---  Nhập thông tin cá nhân ---")
name = input("Nhập tên của bạn: ")
age = input("Nhập tuổi của bạn: ")
job = input("Nhập nghề nghiệp của bạn: ")

# Khởi tạo dictionary với dữ liệu vừa nhập
person = {
    "name": name,
    "age": age,
    "job": job
}
print("\n=> Thong tin :", person)



print("---  Thêm Email ---")
email_input = input("Nhập địa chỉ email muốn thêm: ")
person["email"] = email_input
print("=> Dictionary sau khi thêm email:", person)
print("-" * 30)


print("---  Cập nhật tuổi ---")
print(f"Đang sửa tuổi từ {person['age']} thành 25...")
person["age"] = 25
print("=> Dictionary sau khi sửa tuổi:", person)
print("-" * 30)


print("---  Xóa nghề nghiệp ---")
if "job" in person:
    # Sử dụng lệnh del như trong trang 11 của slide bài giảng
    del person["job"]
    print("=> Đã xóa khóa 'job' thành công.")
else:
    print("=> Không tìm thấy khóa 'job' để xóa.")


print("\n=> DICTIONARY CUỐI CÙNG:", person)
print("-" * 30)