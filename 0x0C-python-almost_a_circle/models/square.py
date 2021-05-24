#!/usr/bin/python3
"""Square file for Almost Circle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Our Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """protype given"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String set up"""
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id,
                                             self.x, self.y, self.width)

    @property
    """This is setting our getter"""

    def size(self):
        return self.width

    @size.setter
    """our setter"""
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """our attribute of upstaed instance"""
        h = [self.id, self.size, self.x, self.y]
        hh = ['id', 'size', 'x', 'y']

        if len(args) >= 1:
            for lo in range(len(args)):
                h[lo] = args[h]
                self.__init__(h[1], h[2], h[3], h[0])
            else:
                for a, b, in kwargs.items():
                    for lo in range(len(hh)):
                        if a == hh[lo]:
                            setattr(self, hh[lo], b)

    def to_dictionary(self):
        """display attr dict"""
        return {"id", self.id, "size": self.width, "x": self.x,
                "y": self.y}
