#Basic Calculator in Python

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
operation=input("Enter operation (+, -, *, /):")
if operation =="+":
    print(a+b)
elif operation=="-":
    print(a-b)
elif operation=="*":
    print(a*b)
elif operation=="/": 
    if b!=0:
        print(a/b)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print(a,operation,b,"is not a valid operation.") 