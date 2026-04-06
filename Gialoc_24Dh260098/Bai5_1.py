file = open("demo.txt", "w") #r đọc, w ghi, a thêm vào cuối file
file.writelines(""" gdsgdadfa
                dsafasf
                Tui la ai
                """)
file.write("Hello world")
file.close()
file = open("demo.txt", "r")
for line in file:
    print(line)
file.close()