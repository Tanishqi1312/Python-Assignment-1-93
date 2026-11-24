"""Assignment 1 - Question 20
Calculate quotient and remainder.
Run this file directly in VS Code.
"""

a = float(input("First number: "))
b = float(input("Second number: "))
if b == 0:
    print("Division by zero is not allowed.")
else:
    print("Quotient =", a // b)
    print("Remainder =", a % b)
