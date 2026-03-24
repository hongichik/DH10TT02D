file = open("demo.csv", "w")
file.writelines("""name,age,gender
                adawfagesgsge""")
file.close()

file = open("demo.csv", "r")
for line in file:
    dong = line.split().split(",")
    if dong.count("") == 0:
        print(dong[1])
file.close()