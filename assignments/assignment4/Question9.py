# numbers divisible by given number in range
start=int(input("enter start:"))
end=int(input("enter end:"))
divisor=int(input("enter divisor:"))
for i in range(start,end+1):
    if i%divisor==0:
        print(i)