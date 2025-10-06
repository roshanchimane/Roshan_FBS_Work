
sub1 = float(input("Enter marks of Subject 1: "))
sub2 = float(input("Enter marks of Subject 2: "))
sub3 = float(input("Enter marks of Subject 3: "))
sub4 = float(input("Enter marks of Subject 4: "))
sub5 = float(input("Enter marks of Subject 5: "))


total_marks = sub1 + sub2 + sub3 + sub4 + sub5
max_marks = 5 * 100   

percentage = (total_marks / max_marks) * 100

print("Percentage:", percentage, "%")
