# age
gender=input("enter gender(male/female):").lower()
age=int(input("enter age:"))

if gender=="male":
    if age>=21:
        print("Eligible")
    else:
        print("Not eligible")
elif gender=="female":
    if age>=18:
        print("eligible")
    else:
        print("not eligible")
else:
    print("invalid gender input")
