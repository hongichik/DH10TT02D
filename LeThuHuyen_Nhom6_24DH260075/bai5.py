file = open("demo.csv", "w")
file.write("""title,author,year
The Great Gatsby,F. Scott Fitzgerald,1925
To Kill a Mockingbird, Harper Lee,1960
1984,George Orwell,1949
            """)
file.close()

file = open("demo.csv", "r")
for line in file:
    dong = line.strip().split(",")
    if dong.count("") == 0:
        print(dong[1])
file.close()