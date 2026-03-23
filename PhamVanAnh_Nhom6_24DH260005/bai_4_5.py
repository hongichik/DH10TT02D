kho={"apple":50,"banana":30,"orange":20}
print(kho)
kho["banana"]=kho["banana"]-10
print("giảm số lương banana",kho)
kho["grape"]=15
print("thêm số lượng grape",kho)
kho=sum(kho.values())
print("tổng",kho)