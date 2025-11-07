def armstrong(num):
    original=num
    digits=len(str(num))
    total=0
    while num>0:
        digit=num%10
        total+=digit**digits
        num//=10
    if original==total:
        print("armstrong")
    else:
        print("Not armstrong")
        
num=153
armstrong(num)

