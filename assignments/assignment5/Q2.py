# percentage of students
n=int(input("enter number of students:"))
total_percent=0
for i in range(n):
    print(f"\n Student {i+1}")
    totalmarks=0
    for j in range(5):
        marks=float(input(f"enter marks for subject {j+1}:"))
        totalmarks+=marks
    percent=totalmarks/5
    print("percentage:",percent)
    total_percent+=percent
avgPercent=total_percent/n
print("Average Percentage:",avgPercent)