import math
radius=20
length=50
breadth=40
costPerM=35

circumference=math.pi*radius 
total=circumference+(length+breadth)

total_Area=total*5
totalCost=total_Area*costPerM

print("Fencing cost:",round(totalCost,2))