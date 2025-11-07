# sum of odd numbers from 1 to n
def sumOdd(n):
    sum=0
    for i in range(n):
        if i%2!=0:
            sum+=i
    return sum
n=int(input("enter n:"))
print(sumOdd(n))