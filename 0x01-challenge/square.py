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
                setattr(self, 'width', args[0])
                setattr(self, 'height', args[1])
            except IndexError:
                raise
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @property
    def width(self):
        """ Getter """
        return self.__width

    @width.setter
    def width(self, val):
        """ Setter """
        if type(val) is int:
            self.__width = val
        else:
            self.__width = 0

    @property
    def height(self):
        """ Getter """
        return self.__height

    @height.setter
    def height(self, val):
        """ Setter """
        if type(val) is int:
            self.__height = val
        else:
            self__height = 0

    def area_of_my_square(self):
        """ Area of the square """
        return self.__width * self.__height

    def PermiterOfMySquare(self):
        """ Compute Perimeter """
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ Pretty print """
        return "{}/{}".format(self.__width, self.__height)


if __name__ == "__main__":

    s = Square(width=12, height=9, asd="adsf")
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())

    s2 = Square(1, True)
    s2.width = 500
    print(s2)
    print(s2.area_of_my_square())
