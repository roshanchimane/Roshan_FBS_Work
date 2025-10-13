# equilateral , isosceles , scalene

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if (a + b > c) and (b + c > a) and (c + a > b):
    print("Valid Triangle")

    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or c == a:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Invalid Triangle")
