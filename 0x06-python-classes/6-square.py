#!/usr/bin/python3
"""Empty class that defines a square"""


class Square:
    """ Empty class that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialization method, this occurs at the beggining of the program

        Keyword Arguments:
            size {int} -- Private attr for the square size (default: {0})
            position {tuple} -- [description] (default: {(0, 0)})
        Raises:
            TypeError: Raise error if the type is not integer
            ValueError: Raise error if the value is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size
            self.position = position

    @property
    def size(self):
        """Getter function for size attr

        Returns:
            int -- Return the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter function for size attr
        Arguments:
            value {int} -- Private attr for the square size
        Raises:
            TypeError: Raise error if the type is not integer
            ValueError: Raise error if the value is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates the area of the square

       Returns:
            int -- Return the area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        self.row = 0
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            while self.row < self.size:
                print("{}{}".format(" " * self.position[0], "#" * self.size))
                self.row += 1
