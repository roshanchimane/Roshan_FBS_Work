def is_leap(year):
    return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

year = int(input("Enter year: "))
print("Leap year" if is_leap(year) else "Not leap year")
