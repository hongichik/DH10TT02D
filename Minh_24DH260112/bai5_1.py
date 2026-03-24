file = open("demo.txt", "w")
file.write("""Hello, 
           Minh""")
file.write("hello word")
file.close()

file = open("demo.txt", "r")
for line in file:
    print(line)
file.close()