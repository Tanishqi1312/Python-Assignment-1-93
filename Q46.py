"""Assignment 1 - Question 46
Accept five subject marks and display total.
Run this file directly in VS Code.
"""

marks = [float(input(f"Subject {i} marks: ")) for i in range(1, 6)]
print("Total marks =", sum(marks))
