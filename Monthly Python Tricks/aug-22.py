"""
Monthly Python Tricks from RealPython Newsletter
AUGUST
"""

"""
TOPIC: Functions are first-class citizens in Python
DATE: 2022/08/01

They can be passed as arguments to other functions,
returned as values from other functions, and 
assigned to variables and stored in data structures.
"""


def add(a, b):
    """ returns sum of two numbers"""
    return a + b


math_operations = [add]
print(math_operations[0])
print(math_operations[0](2, 3))
