#!/usr/bin/python3
'''Square Class'''


class Square:
    '''square private instance attritute size'''
    def __init__(self, size=0, position=(0, 0)):
        '''instantiation with size'''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''size getter'''
        return self.__size

    @size.setter
    def size(self, value):
        '''size setter'''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        '''getter for position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''sets a position of a square'''
        if type(value) is not tuple or value[0] < 0 or value[1] < 0 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        '''returns the current square area'''
        return self.__size ** 2

    def my_print(self):
        '''print square with "#" character'''
        if self.size == 0:
            print("")
        if self.position[1] > 0:
            for i in range(self.position[1]):
                print("")
        for i in range(self.__size):
            print("{}".format(" " * self.position[0]), end="")
            for j in range(self.size):
                print('#', end="")
            print("")
