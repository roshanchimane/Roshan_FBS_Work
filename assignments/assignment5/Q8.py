# 1! + 2! + 3! + … + n!
import math
n = int(input("Enter n: "))

sum_fact=0
for i in range(1,n+1):
    sum_fact+=math.factorial(i)
print("Sum:",sum_fact)

# N + N² + N³ + … + Nᴺ
sum_series=0
for i in range(1,n+1):
    sum_series+= n**i
print("Series sum is:", sum_series)

#Geometric series (ratio = 2)
geo_series=0
for i in range(1,n+1):
    geo_series+=2**i
print("Geometric ratio:",geo_series)

# S = a + a²/2 + a³/3 + … + a¹⁰/10
a = int(input("Enter value of a: "))
S = 0
for i in range(1, 11):
    S += (a ** i) / i
print("Sum =", S)

#x - x²/3 + x³/5 - x⁴/7 + … up to n terms
x = float(input("Enter x: "))
n = int(input("Enter number of terms: "))
S = 0
sign = 1
den = 1

for i in range(1, n+1):
    S += sign * (x ** i) / den
    sign *= -1
    den += 2

print("Sum =", S)
