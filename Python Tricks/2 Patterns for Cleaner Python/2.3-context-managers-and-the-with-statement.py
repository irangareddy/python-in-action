"""2.3 Context Managers and the with Statement"""

with open('message.txt', 'w') as f:
    f.write('Hello World!')

"""
Internally, the above code sample translates to something like this:

f = open('hello.txt', 'w')
try:
    f.write('hello, world')
finally:
    f.close()
"""
