def calculator(num1,num2,operation):
    if operation == 'add':
       print(f"addition:",a+b)

    elif operation == 'sub':
        print(f"subtraction:",a-b)

    elif operation == 'mult':
        print("multiplication:",a*b)

    elif operation == 'div':
        if b != 0:
            print("division:",a/b)
        else:
            print("error, Division by 0 ")

a=int(input("enter the number, a:"))
b=int(input("enter the number, b:"))
operation=input("enter the operator{add/sub/mult/div}:").lower()

calculator(a,b,operation)
