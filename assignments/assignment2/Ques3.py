feet = int(input("Enter feet: "))
inches = int(input("Enter inches: "))

total_cm = (feet * 30.48) + (inches * 2.54)
meters = total_cm / 100
centimeters = total_cm % 100

print("Meters:", int(meters), "Centimeters:", centimeters)
