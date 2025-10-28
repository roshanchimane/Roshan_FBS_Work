#painting
length=int(input("enter length:"))

breadth=int(input("enter breadth:"))

height=int(input("enter height:"))
cost=int(input("enter cost per cm:"))

totalArea=2*height*(length+breadth)
totalCost=totalArea*cost
print("Total Cost:",totalCost)