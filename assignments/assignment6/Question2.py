# number right angled triangle - pattern2
n=4
s=1
for i in range(n):
    for j in range(i+1):
        print(s,end=" ")
        s+=1
    print()