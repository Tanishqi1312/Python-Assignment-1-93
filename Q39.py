"""Assignment 1 - Question 39
Demonstrate type() with string, list, tuple and dictionary.
Run this file directly in VS Code.
"""

text = "hello"
items = [1, 2]
values = (3, 4)
data = {"x": 5}
for value in (text, items, values, data):
    print(type(value))
