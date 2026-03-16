c ="c734 9bc2 d65ca 92 65bf bc8343 6e5 e868"
def demkhoangtrang(c):
    print("- Số lượng khoảng trắng là: ")
    c1 = c.count(" ")
    print(c1)
def demso4(c):
    print("- Số lượng số 4 là: ")
    c2 = c.count("4")
    print(c2)
def thayso(c):
    print("-Thêm số có chữ 'số'")
    kq = ""
    for a in c:
        if a.isdigit():
            kq += " số " + a
        else:
            kq += a
    print(kq)
demkhoangtrang(c)
demso4(c)
print(thayso(c))