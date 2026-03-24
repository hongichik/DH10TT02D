file = open("demo.txt", "w")
file.write("""Hello, 
           Vinh Hoang""")
file.write("Alo")
file.close()

file = open("demo.txt", "r")
for line in file:
    print(line)
file.close()