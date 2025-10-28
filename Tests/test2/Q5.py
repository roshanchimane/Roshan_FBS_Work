prices=[]
for i in range(5):
    p=float(input(f"enter price for element{i+1}:"))
    prices.append(p)
    
total=sum(prices)
gst=total*0.18

totalPrice=total+gst
print("GST:",gst)
print("Total price:",totalPrice)