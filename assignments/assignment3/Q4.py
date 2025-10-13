# check if its valid triangle(sides)
n1=int(input("enter first side:"))
n2=int(input("enter second side:"))
n3=int(input("enter third side:"))
if(n1+n2>n3) and (n2+n3>n1) and (n1+n3>n2):
    print("Valid triangle")
else:
    print("Not a Valid triangle")