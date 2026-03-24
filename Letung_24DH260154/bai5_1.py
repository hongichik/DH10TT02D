file = open("demo.txt", "w") #r đọc, w ghi, a thêm vào cuối file
file.writelines(""" Hello 
                Huhu
                """)
file.write("Hello world")
file.close()
file = open("demo.txt", "r")
for line in file:
    print(line)
file.close()