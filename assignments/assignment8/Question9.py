def palindromecheck(num):
    return str(num)==str(num)[::-1]
num=123231
print("palindrome"if palindromecheck(num) else "not palindrome")
