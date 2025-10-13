# captcha
import random
username=input("enter username:")
password=input("enter password:")

cor_user="admin"
cor_pass="12345"

if username==cor_user and password==cor_pass:
    print("login success")
    captcha=random.randint(1000,9999)
    print("captcha:",captcha)
    
    usercaptcha=int(input("enter captcha:"))
    if usercaptcha==captcha:
        print("Captcha Correct")
    else:
        print("Captcha Incorrect")
else:
    print("invalid username or passwod")