file = open("demo.csv", "w")
file.writelines("""Name, Age, Gender
loc ga mo""")
file.close()
file = open("demo.csv", "r")
for line in file:
    dong = line.strip().split(",")
    if dong.count("") ==0:
        print(dong[1])
file.close()

                              