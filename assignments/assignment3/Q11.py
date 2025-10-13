
ticket_price = float(input("Enter ticket price per person: "))

total_amount = 0 
for i in range(1, 6):
    age = int(input(f"Enter age of person {i}: "))
    
    if age < 12:
        discount = 0.30 
    elif age > 59:
        discount = 0.50  
    else:
        discount = 0.0   
    
    person_amount = ticket_price * (1 - discount)
    total_amount += person_amount

print("\nTotal amount to be paid for 5 people: Rs.", total_amount)
