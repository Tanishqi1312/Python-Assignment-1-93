"""Assignment 1 - Question 15
Calculate total and average of five subject marks.
Run this file directly in VS Code.
"""

marks = [float(input(f"Enter marks for subject {i}: ")) for i in range(1, 6)]
total = sum(marks)
print("Total =", total)
print("Average =", total / 5)
