# divisible by 5 and 7 in range
start=int(input("enter start:"))
end=int(input("enter end:"))
for i in range(start,end+1):
    if i%7==0 and i%5==0:
        print(i)