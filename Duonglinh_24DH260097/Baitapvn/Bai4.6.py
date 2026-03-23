    # Tạo danh bạ 
phonebook = {
    "An": "0901234567",
    "Binh": "0912345678",
    "Cuong": "0923456789"
}

# xem cua Bình
if "Binh" in phonebook:
    print("Số của Bình là: ",phonebook["Binh"])

#Xoa Cuong
del phonebook["Cuong"]

#in lai
print("Danh bạ", phonebook  )