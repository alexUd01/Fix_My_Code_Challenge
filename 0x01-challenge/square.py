#!/usr/bin/python3
""" Square module: challenge """


class Square():
    """ Square Class """

    __width = 0
    __height = 0

    def __init__(self, *args, **kwargs):
        """ Initializations """
        if args:
            try:
                self.width = args[0]
                self.height = args[1]
            except IndexError:
                raise  # pass
        elif kwargs:
            self.width = kwargs.get('width', 0)
            self.height = kwargs.get('height', 0)

    @property
    def width(self):
        """ Getter """
        return self.__width

    @width.setter
    def width(self, val):
        """ Setter """
        if type(val) is int:
            if val < 0:
                raise ValueError('width must be >= 0')
            self.__width = val
        else:
            raise TypeError('width must be an integer')

    @property
    def height(self):
        """ Getter """
        return self.__height

    @height.setter
    def height(self, val):
        """ Setter """
        if type(val) is int:
            if val < 0:
                raise ValueError('width must be >= 0')
            self.__height = val
        else:
            raise TypeError('height must be an integer')

    def area_of_my_square(self):
        """ Area of the square """
        return self.__width * self.__height

    def PermiterOfMySquare(self):
        """ Compute Perimeter """
        return 2 * (self.__width  + self.__height)

    def __str__(self):
        """ Pretty print """
        return "{}/{}".format(self.__width, self.__height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())

    s2 = Square(1, -1)
    s2.width = 500
    print(s2)
    print(s2.area_of_my_square())

    s3 = Square()
    print(s3)

    print()

    print(Square(4, 3))
    print(Square(4, 3).area_of_my_square())
    print(Square(4, 3).PermiterOfMySquare())
