"""
monthly_python_tricks from RealPython Newsletter
AUGUST
"""

"""
TOPIC: Functions are first-class citizens in Python
DATE: 2022/08/01

They can be passed as arguments to other functions,
returned as values from other functions, and
assigned to variables and stored in data structures.
"""


def add(first_number, second_number):
    """ returns sum of two numbers"""
    return first_number + second_number


math_operations = [add]
print(math_operations[0])
print(math_operations[0](2, 3))

"""
TOPIC: Python has first-class functions
they can be used to emulate switch/case statements
DATE: 2022/08/05

"""


def dispatch_if(operator, first_value, second_value):
    """use if to switch case"""
    if operator == 'add':
        return first_value + second_value
    if operator == 'sub':
        return first_value - second_value
    if operator == 'mul':
        return first_value * second_value
    if operator == 'div':
        return first_value / second_value

    return None


def dispatch_dict(operator, first_value, second_value):
    """use dict to switch case"""
    return {
        'add': lambda: first_value + second_value,
        'sub': lambda: first_value - second_value,
        'mul': lambda: first_value * second_value,
        'div': lambda: first_value / second_value,
    }.get(operator, lambda: None)()


print(dispatch_if('add', 5, 1))
print(dispatch_dict('add', 5, 1))
print(dispatch_if('unknown', 5, 1))
print(dispatch_dict('unknown', 5, 1))

"""
TOPIC: Python has a HTTP server
DATE: 2022/08/09


Python has a HTTP server built into the standard library.
This is super handy for previewing websites

Python 3.x
$ python3 -m http.server

Python 2.x
$ python -m SimpleHTTPServer 800
(This will serve the current directory at http://localhost:8000)
"""
