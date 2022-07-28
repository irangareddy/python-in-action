"""
Monthly Python Tricks from RealPython Newsletter
JULY
"""

import operator
import timeit

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
Test for [Truthiness](https://www.pythonmorsels.com/truthiness/#:~:text=Truthiness%20is%20also%20about%20non%2Dzeroness&text=So%20if%20we%20check%20the,number%20not%20equal%20to%20zero.&text=That%20if%20statements%20prints%20no,which%20means%20zero%20is%20falsey.&text=Every%20number%20other%20than%200%20is%20truthy.)
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

# import operator
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
    return "Hi %s!" % name_of_userid.get(user_id, "there")


print(greeting(user_id=1))
print(greeting(user_id=22))

"""
TOPIC: timeit module
DATE: 2022/07/23
"""

# import timeit

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
temp = a
a = b
b = temp

# shorthand
a, b = b, a
