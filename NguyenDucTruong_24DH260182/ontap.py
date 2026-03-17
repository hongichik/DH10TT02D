chuoi = "Nguyễn Đức Trường"
print(chuoi.ljust(30,"-"))
print(chuoi.rjust(30,"-"))
print(chuoi.center(30,"-"))
print(chuoi.__len__()) # đếm số ký tự
chuoi= chuoi.upper()
print(chuoi)
chuoi = chuoi.lower()
print(chuoi)
s="#Hello World*"
print(s.strip("#*")) # xóa ký tự ở đầu và cuối chuỗi
print(s.lstrip("#")) # xóa ký tự ở đầu chuỗi
print(s.rstrip("*")) # xóa ký tự ở cuối chuỗi
print(s.split()) # tách chuỗi thành danh sách các từ
print(s.replace(" ", "_")) # thay thế khoảng trắng bằng dấu gạch dưới
print(s.find("World")) # tìm vị trí của chuỗi con "World"
print(s.count("o")) # đếm số lần xuất hiện của ký tự "o"
print(s.startswith("#")) # kiểm tra xem chuỗi có bắt đầu bằng "#" không
print(s.endswith("*")) # kiểm tra xem chuỗi có kết thúc bằng "*" không
print(s.isalpha()) # kiểm tra xem chuỗi có phải là chữ cái không
print(s.isdigit()) # kiểm tra xem chuỗi có phải là số không
print(s.isalnum()) # kiểm tra xem chuỗi có phải là chữ cái hoặc số không
print(s.isupper()) # kiểm tra xem chuỗi có phải là chữ hoa không
print(s.islower()) # kiểm tra xem chuỗi có phải là chữ thường không
print(s.isspace()) # kiểm tra xem chuỗi có phải là khoảng trắng không
print(s.title()) # chuyển đổi chuỗi thành dạng tiêu đề (mỗi từ bắt đầu bằng chữ hoa)
print(s.capitalize()) # chuyển đổi chuỗi thành dạng chỉ có chữ cái đầu tiên là chữ hoa
print(s.swapcase()) # chuyển đổi chữ hoa thành chữ thường và ngược lại