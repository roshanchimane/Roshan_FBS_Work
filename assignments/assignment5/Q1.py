# username password entering 3 time chance
correctID="roshan"
correctPassword="12345"
for i in range(3):
    userID=input("enter ID:")
    userPass=input("enter Password:")
    if userID==correctID and userPass==correctPassword:
        print("Logged in Successfully")
    else:
        print("invalid credentials,enter again")
else:
    print("Access Denied.")