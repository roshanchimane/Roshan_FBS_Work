# profit or loss
cp=int(input("enter cost price:"))
sp=int(input("enter selling price:"))
if cp<sp:
    print("profit =",sp-cp)
else:
    print("loss =",sp-cp)