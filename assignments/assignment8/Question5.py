# primes in range
def isPrime(num):
    if num<2:
        isPrime=False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
def inrange(n):
    sum=0
    for i in range(2,n+1):
        if isPrime(i):
            sum+=i
    return sum
n=int(input("enter n:"))
print("Sum of primes:",inrange(10))