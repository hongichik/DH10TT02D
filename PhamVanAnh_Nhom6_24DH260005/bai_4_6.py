danh_ba={"An":"0901234567","Bình":"0912345678","Cường":"0923456789"}
print(danh_ba)
print("Danh bạ: ",danh_ba)
if "Bình" in danh_ba:
    print(f"Số điện thoại của Bình là: {danh_ba['Bình']}")
else:
    print("Không tìm thấy tên Bình trong danh bạ!")

if "Cường" in danh_ba:
    del danh_ba["Cường"]
print("Danh bạ sau khi cập nhật: ",danh_ba)