""" Multiple Inheritance """

"""
TOPIC: Object and Class
DATE: 2022/10/11
"""


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

    def what_am_i(self):
        """returns the type of the object"""
        return '📸 RECTANGLE'


big_box = Rectangle(length=4, width=8)
print(f'{big_box.what_am_i()}: The big box of length'
      f' {big_box.length} and width {big_box.width} '
      f'has area: {big_box.area()} and perimeter: {big_box.perimeter()}')

"""
TOPIC: Simple Inheritance
DATE: 2022/10/11
"""


class Square(Rectangle):
    """ Square Shape """

    def __init__(self, length):
        """ create a square with specified length """
        super().__init__(length, length)

    def what_am_i(self):
        """returns the type of the object"""
        return '⬜ SQUARE'


box = Square(length=4)
print(f'{box.what_am_i()}: The box of length {box.length}'
      f'has area: {box.area()} and perimeter: {box.perimeter()}')


class Cube(Square):
    """ Shape: Cube """

    def surface_area(self):
        """ Returns surface area """
        area = self.area()
        return area * 6

    def volume(self):
        """ Returns Volume """
        area = super().area()
        return area * self.length

    def what_am_i(self):
        """returns the type of the object"""
        return '📦 CUBE'

    def family_tree(self):
        """returns the family tree"""
        return self.what_am_i() + ' child of ' + super().what_am_i()


full_box = Cube(length=24)
print(f'{full_box.what_am_i()}: The box of length'
      f' {full_box.length} has area: {full_box.area()} perimeter:'
      f' {full_box.perimeter()}, surface area: {full_box.surface_area()}'
      f' and volume: {full_box.volume()}')

print(full_box.family_tree())
