# armstrong in rangee
start = int(input("Enter start: "))
end = int(input("Enter end: "))

for num in range(start, end+1):
    temp = num
    order = len(str(num))
    sum_powers = 0
    while temp > 0:
        digit = temp % 10
        sum_powers += digit ** order
        temp //= 10
    if sum_powers == num:
        print(num)
