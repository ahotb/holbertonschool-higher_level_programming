#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def area(self):
        """
                Docstring for area

                :param self: Description
                """
        pass

    @abstractmethod
    def perimeter(self):
        """
                Docstring for perimeter

                :param self: Description
                """
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
                Docstring for area

                :param self: Description
                """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
                Docstring for perimeter

                :param self: Description
                """
        return 2 * math.pi * self.radius


class Rectangle(Shape):

    def __init__(self, width, height):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.height = height

    def area(self):
        """
                Docstring for area

                :param self: Description
                """
        return self.width * self.height

    def perimeter(self):
        """
                Docstring for perimeter

                :param self: Description
                """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)


def shape_info(shape):
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
