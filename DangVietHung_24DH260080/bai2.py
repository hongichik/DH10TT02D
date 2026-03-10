while True:
    demchan =0
    demle = 0 

    so =  int(input("nhập số nguyên dương n:"))
    if so == 0:
        print ("kết thúc chương trình.")
        break
    if so %2 ==0:
        demchan += 1
    else:
        demle += 1
    print("Số lương chẵn là :",demchan)
    print("Số lương lẻ là :",demle)