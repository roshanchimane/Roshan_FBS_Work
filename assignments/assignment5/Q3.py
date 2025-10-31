# ticket costing
passengers=int(input("enter number of passengers:"))
ticketCost=int(input("enter 1 ticket cost:"))
total_Amount=0
for i in range(passengers):
    age=int(input(f"enter Age of passenger {i+1}:"))
    if age<12:
        total_Amount+=ticketCost*0.7
    elif age>59:
        total_Amount+=ticketCost*0.5
    else:
        total_Amount+=ticketCost
print("Total Amount of tickets is:",total_Amount)