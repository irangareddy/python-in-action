""" Multiple Inheritance """

"""
TOPIC: Object and Class
DATE: 2022/10/11
"""


class Square:
    """ Square Shape """

    def __init__(self, length):
        """ create a square with specified length """
        self.length = length

    def area(self):
        """returns the area"""
        return self.length * self.length

    def perimeter(self):
        """returns the perimeter"""
        return 4 * self.length


box = Square(length=4)
print(f'The box of length {box.length} '
      f'has area: {box.area()} and perimeter: {box.perimeter()}')
