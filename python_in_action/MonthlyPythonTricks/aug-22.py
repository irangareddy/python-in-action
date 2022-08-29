"""
MonthlyPythonTricks from RealPython Newsletter
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

"""
TOPIC: Python has first-class functions
they can be used to emulate switch/case statements
DATE: 2022/08/05
"""


def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y
    else:
        return None


def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
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
