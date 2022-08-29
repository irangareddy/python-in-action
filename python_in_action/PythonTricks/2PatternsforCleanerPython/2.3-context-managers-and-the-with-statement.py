"""2.3 Context Managers and the with Statement"""
import threading

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

some_lock = threading.Lock()

# Harmful:
some_lock.acquire()
try:
    print('Inside Try')
finally:
    some_lock.release()

# Better:
with some_lock:
    print('using with while threading')

"""
Note:
The with statement can make code that deals with
system resources more readable. It also helps you avoid
bugs or leaks by making it practically impossible to forget
to clean up or release a resource when it’s no longer needed.
"""
