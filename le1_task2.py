temp=float(input("enter the temperature:"))
unit=input("enter the unit(c for celsius, f for fahrenheit):").strip().lower()
if unit=='c':
    covert=(temp * 9/5)+32
    print(f"{temp}c is equal to{covert}F")
elif unit=='f':
    covert=(temp-32)*5/9
    print(f"{temp}c is equal to {covert}C")
else:
    print("invalid input,enter the unit (c for celsius,f for fahrenheit)")

