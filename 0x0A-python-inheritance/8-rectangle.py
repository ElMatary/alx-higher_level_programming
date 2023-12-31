#!/usr/bin/python3
'''module for Rectangle class '''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle subclass'''
    def __init__(self, width, height):
        '''Constractor'''
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
