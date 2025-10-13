# check if its valid triangle(angles)
n1=int(input("enter first angle:"))
n2=int(input("enter second angle:"))
n3=int(input("enter third angle:"))
if(n1+n2+n3)==180:
    print("Valid triangle")
else:
    print("Not a Valid triangle")