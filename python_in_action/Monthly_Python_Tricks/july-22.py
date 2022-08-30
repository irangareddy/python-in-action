"""
Monthly_Python_Tricks from RealPython Newsletter
JULY
"""
import json
import operator
import timeit
from collections import namedtuple

"""
TOPIC: unpacking generalizations
DATE: 2022/06/29
"""
# Python 3.5+
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

z = {**x, **y}
# same keys are replaced by latest value
print(z)

# Python 2.x
z = dict(x, **y)
print(z)

# TODO: learn unpacking generalizations

"""
TOPIC: Different ways to test multiple flags at once
DATE: 2022/06/30
"""

a, b, c = 0, 1, 0

# pass if any of the value is equal to 1

# regular
if a == 1 or b == 1 or c == 1:
    print("PASSED")

# with tuple
if 1 in (a, b, c):
    print("PASSED")

"""
Test for [Truthiness](https://www.pythonmorsels.com/truthiness/#:~:text=Truthiness%20is%20also%20about%20non%2Dzeroness&text=So%20if%20we%20check%20the,number%20not%20equal%20to%20zero.&text=That%20if%20statements%20prints%20no,which%20means%20zero%20is%20falsey.&text=Every%20number%20other%20than%200%20is%20truthy.) # noqa: E501
"""
if a or b or c:
    print("PASSED")

if any((a, b, c)):
    print("PASSED")

"""
TOPIC: sort a Python dict by value
DATE: 2022/07/01
"""

unsorted_dict = {'a': 4, 'c': 2, 'b': 3, 'd': 1}
print(unsorted_dict)
# 1 here represents the values
sorted_dict = sorted(unsorted_dict.items(), key=lambda value: value[1])
print(sorted_dict)

# importing operator
sorted_dict = sorted(unsorted_dict.items(), key=operator.itemgetter(1))
print(sorted_dict)

# TODO: lamda and operator module

"""
TOPIC: The get() method on Python dict and its default args
DATE: 2022/07/04
"""
name_of_userid = {
    1: "Ranga",
    7623: "Vikram",
    983: "Matt Nelson",
}


def greeting(user_id):
    """Greeting a user function"""
    return f'Hello, {user_id}'


print(greeting(user_id=1))
print(greeting(user_id=22))

"""
TOPIC: NamedTuple from collections
DATE: 2022/07/13
"""

Car = namedtuple('Car', 'color mileage seats')
my_car = Car('red', 100, 2)

print(my_car)
print(my_car.color, my_car.mileage, my_car.seats)

"""
TOPIC: json.dumps() to pretty print the dict
DATE: 2022/07/17
"""

for_json_dict = {'a': 23, 'b': 42, 'c': 0xc0ffee}
print(for_json_dict, '😔 # No Indentation')

pretty_dict = json.dumps(for_json_dict, indent=4, sort_keys=True)
print(pretty_dict)
# Note: dict key must be from primitive types
# RAISES ERROR: TypeError: keys must be
# str, int, float, bool or None, not builtin_function_or_method
# json.dumps({all: 'yup'})

# TODO: pprint module

"""
TOPIC: Function argument unpacking
DATE: 2022/07/20
"""


def func_arg_unpack(m, n, o):
    """Function argument unpacking"""
    print(m, n, o)


tuple_vec = (1, 0, 1)
dict_vec = {'m': 1, 'n': 0, 'o': 2}
# RAISES ERROR: dict_vec = {'m': 1, 'n': 0, 'z': 2}

func_arg_unpack(*tuple_vec)
func_arg_unpack(**dict_vec)

"""
TOPIC: timeit module
DATE: 2022/07/23
"""

# importing timeit

exec_time = timeit.timeit('"-".join(str(n) for n in range(100))',
                          number=10000)
print(exec_time)

# TODO: timeit https://www.geeksforgeeks.org/timeit-python-examples/

"""
TOPIC: Shorthand for in-place value swapping
DATE: 2022/07/26
"""

a = 43
b = 23

# swap values
# pylint: disable=consider-swap-variables
temp = a
a = b
b = temp

# shorthand
a, b = b, a

"""
TOPIC: "is" vs "=="
DATE: 2022/07/29
"""

list_of_integers = [1, 2, 3]
list_of_copy = list_of_integers

print(list_of_copy is list_of_integers)
print(list_of_copy == list_of_integers)

listed_copy = list(list_of_integers)

print(listed_copy is list_of_integers)
print(listed_copy == list_of_integers)

"""
Note:
• "is":expressions evaluate to True
if two variables point to the same object
• "==": evaluates to True if the objects
referred to by the variables are equal
"""
