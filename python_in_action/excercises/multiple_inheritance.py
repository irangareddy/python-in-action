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


class Rectangle:
    """ Rectangle Shape """

    def __init__(self, length, width):
        """ create a rectangle with specified length """
        self.length = length
        self.width = width

    def area(self):
        """returns the area"""
        return self.length * self.width

    def perimeter(self):
        """returns the perimeter"""
        return 4 * self.length


big_box = Rectangle(length=4, width=8)
print(f'The big box of length {big_box.length} and width {big_box.width} '
      f'has area: {big_box.area()} and perimeter: {big_box.perimeter()}')
