def sumOfDigits(n):
    total=0
    while n>0:
        digit=n%10
        total+=digit
        n=n//10
    return total
n=int(input("enter n:"))
print(f"Sum of digits of num {n} :",sumOfDigits(n))