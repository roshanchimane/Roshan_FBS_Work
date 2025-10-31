# armstrong or not check
num=int(input("enter number:"))

original=num
digits=len(str(num))
res=0
while num>0:
    digit=num%10
    res+=digit**digits
    num//=10
    
if res==original:
    print("armstrong")
else:
    print("Not armstrong")
    