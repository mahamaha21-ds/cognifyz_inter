text=input("enter a palindrome:")
checked=text.replace("","").lower()
if checked==checked[::-1]:
    print("palindrome")
else:
    print("not palindrome")