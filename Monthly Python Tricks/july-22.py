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


