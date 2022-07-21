"""
Monthly Python Tricks from RealPython Newsletter
JULY
"""

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
