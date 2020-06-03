#!/usr/bin/python
'''Rectangle module'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry
'''import from exercise 7-base_geometry'''


class Rectangle(BaseGeometry):
    '''class Rectangle'''
    def __init__(self, width, height):
        '''initialize constructor'''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
