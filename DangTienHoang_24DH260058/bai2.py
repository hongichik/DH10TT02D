chan = 0
le = 0

while True:
    n = int(input("Nhap so (0 de dung): "))

    if n == 0:
        break
    elif n % 2 == 0:
        chan += 1
    else:
        le += 1

print("So luong so chan:", chan)
print("So luong so le:", le)
