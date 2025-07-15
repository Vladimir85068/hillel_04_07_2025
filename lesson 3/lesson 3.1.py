import math

nd = float(input("Enter first number: "))
r = float(input("Enter second number: "))

action = input("Enter action (+, -, *, /): ")

if action == "+":
    print(nd + r)

elif action == "-":
    print(nd - r)

elif action == "*":
    print(nd * r)

elif action == "/":
    print(nd / r)
    if r == 0:
        print("Error! You cannot divide by zero!")