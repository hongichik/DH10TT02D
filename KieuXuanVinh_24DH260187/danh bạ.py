danh_ba = {
    "AN": "0901234567",
    "BINH": "0912345678",
    "CUONG": "0923456789",
}
print("Danh bạ:", danh_ba)
if "BINH" in danh_ba:
    print("Số điện thoại của BINH:", danh_ba["BINH"])
else:
    print("Không tìm thấy BINH trong danh bạ.")

del danh_ba["CUONG"]
print("Danh bạ sau khi xóa CUONG:", danh_ba)
print("Danh bạ sau khi cập nhật:    ", )
for ten, sdt in danh_ba.items():
    print(ten, ":", sdt)
