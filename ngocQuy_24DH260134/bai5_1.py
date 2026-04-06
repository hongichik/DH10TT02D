file = open("demo.txt", "w") #r đọc, w ghi, a thêm vào cuối file
file.write("""abcd
           efgh
           ijkl""")
file.write("Thầy hồng")
file.close()

file = open("demo.txt", "r")
for line in file:
    print(line)
file.close()