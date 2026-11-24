"""Assignment 1 - Question 14
Calculate simple interest.
Run this file directly in VS Code.
"""

principal = float(input("Enter principal: "))
rate = float(input("Enter annual rate (%): "))
time = float(input("Enter time in years: "))
print("Simple Interest =", principal * rate * time / 100)
