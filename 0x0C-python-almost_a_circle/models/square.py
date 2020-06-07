#!/usr/bin/python3
'''square module'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''class square'''
    def __init__(self, size, x=0, y=0, id=None):
        '''initilize constructor with attributes'''
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        '''string representation of an instance'''
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.height)
