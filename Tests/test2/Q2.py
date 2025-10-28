num=int(input("enter 3 digit number:"))
if 100<=num<=999:
    first=num //100
    second=(num//10)%10
    third=num%10
    if first==2*second and first*2==third:
        print("Done,You got it")
    else:
        print("Try next time")
else:
    print("Not a 3 digit number")