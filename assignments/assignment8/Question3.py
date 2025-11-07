# adding numbers till n
def numAdd(n):
    return n*(n+1)//2
n=int(input("enter n:"))
print("Sum of numbers:",numAdd(n))

# sum Factorial
import math
def sumFactorial(n):
    return sum(math.factorial(i) for i in range(1,n+1))

n=int(input("enter n:"))
print("Sum of factorial:",sumFactorial(n))

# sum power
def sumPower(n):
    return sum(i*i for i in range(1,n+1))
n=int(input("enter n:"))
print(sumPower(n))