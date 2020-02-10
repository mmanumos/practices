#!/bin/usr/python3
""" Second class """

from models.base import Base


class Rectangle(Base):
    """ Rectangle class inheritance of Base class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor function to Rectangle """
        super().__init__(id)
        width = width
        height = height
        x = x
        y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        pass

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        pass

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        pass

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        pass
