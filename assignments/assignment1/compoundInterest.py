
P = float(input("Enter the Principal amount: "))
R = float(input("Enter the Rate of Interest (in %): "))
T = float(input("Enter the Time (in years): "))

A = P * (1 + R/100) ** T
CI = A - P


print("Compound Interest:", CI)
print("Total Amount:", A)
