#!/usr/bin/python3
"""Given Module to contain rectangle information"""


from models.base import Base
import inspect


class Rectangle(Base):
    """Rect inherits child base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    def area(self):
            """obtain area of rect"""

            return self.height * self.width

    def to_dictionary(self):
        """rtrn dict reprsnt of Rect"""

        webster = {}
        for h in inspect.getmembers(self):
            if not h[0].startswith("_"):
                if not inspect.ismethod(i[1]) and\
                   not inspect.isfunction(h[1]):
                    webster[h[0]] = h[1]
        return webster

    @property
    def width(self):
        """getter for width"""

        return self.__width

    @width.setter
    def width(self, value):
        """My setter"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""

        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x"""

        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""

        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

        def __str__(self):
            """string format"""

            stg = "[Rectange] ({}) ".format(self.id)
            stg2 = "{}/{} - {}/{}".format(self.__x, self.__y, self.width,
                                          self.__height_)

            return stg + stg2

    def update(self, *args, **kwargs):
        """update rect values"""

        indx = [self.id, self.__width, self.__height, self.__x, self.__y]
        if len(args) >= 1:
            for h in range(len(args)):
                indx[h] = args[h]
            else:
                for h in kwargs:
                    if h == 'id':
                        indx[0] = kwargs[h]
                    if h == 'width':
                        indx[1] = kwargs[h]
                    if h == 'height':
                        indx[2] = kwargs[h]
                    if h == 'x':
                        indx[3] = kwargs[h]
                    if h == 'y':
                        indx[4] = kwargs[h]
            self.__init__(indx[1], indx[2], indx[3], indx[4], indx[0])

    def display(self):
        """print stdout Rect"""

        for sides in range(self.__y):
            print()
        for rows in range(0, self.__height):
            print("{}{}".format(' ' * self.__x, "#" * self.width))
