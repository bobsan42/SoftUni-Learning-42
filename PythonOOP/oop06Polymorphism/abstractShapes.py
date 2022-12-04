from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

    # def converted_area(self):


# TODO: Implement Circle and Rectangle

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self._radius = radius

    def calculate_area(self):
        return pi * self._radius ** 2

    def calculate_perimeter(self):
        return 2 * pi * self._radius


class Rectangle(Shape):
    def __init__(self, height, width):
        super().__init__()
        self._height = height
        self._width = width

    def calculate_perimeter(self):
        return 2 * (self._height + self._width)

    def calculate_area(self):
        return self._width * self._height


circle = Circle(5)
# print(circle.calculate_area())
# print(circle.calculate_perimeter())
print()
rectangle = Rectangle(10, 20)
# print(rectangle.calculate_area())
# print(rectangle.calculate_perimeter())

shape_list = [circle, rectangle]
for obj in shape_list:
    print(type(obj))
    print('is Shape: ' + str(isinstance(obj, Shape)))
    print('is Circle: ' + str(isinstance(obj, Circle)))
    print('is Rectangle: ' + str(isinstance(obj, Rectangle)))
    print('Perimeter: ' + str(obj.calculate_perimeter()))
    print('Area: ' + str(obj.calculate_area()))
    print('*' * 50)
