# finding area and perimeter of shape 

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
radius = float(input("Enter radius: "))

# Area
area = (length * breadth) + (0.5 * 3.14 * radius ** 2)

# Perimeter
perimeter = (2 * length) + (2 * breadth - 2 * radius) + (3.14 * radius)

print("Area =", area)
print("Perimeter =", perimeter)
