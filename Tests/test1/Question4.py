def wall_area(length, breadth, height):
    return 2 * height * (length + breadth)

# Room 1 input
l1 = float(input("Enter length of room 1: "))
b1 = float(input("Enter breadth of room 1: "))
h1 = float(input("Enter height of room 1: "))

# Room 2 input
l2 = float(input("Enter length of room 2: "))
b2 = float(input("Enter breadth of room 2: "))
h2 = float(input("Enter height of room 2: "))

# Painting costs
cost_interior = float(input("Enter cost per unit area for interior painting: "))
cost_exterior = float(input("Enter cost per unit area for exterior painting: "))

# Wall areas
area1 = wall_area(l1, b1, h1)
area2 = wall_area(l2, b2, h2)
total_area = area1 + area2

# Painting cost
interior_cost = total_area * cost_interior
exterior_cost = total_area * cost_exterior
total_cost = interior_cost + exterior_cost

print("\n--- Painting Cost ---")
print("Wall Area of Room 1 =", area1)
print("Wall Area of Room 2 =", area2)
print("Total Wall Area =", total_area)
print("Interior Painting Cost =", interior_cost)
print("Exterior Painting Cost =", exterior_cost)
print("Total Painting Cost =", total_cost)
