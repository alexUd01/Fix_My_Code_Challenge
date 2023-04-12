#!/usr/bin/python3
""" Square module: challenge """


class square():
    """ Square Class """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Initializations """
        if args:
            try:
                if type(args[0]) is int:
                    setattr(self, 'width', args[0])
                else:
                    setattr(self, 'width', 0)
                if type(args[1]) is int:
                    setattr(self, 'height', args[1])
                else:
                    setattr(self, 'height', 0)
            except IndexError:
                raise
        elif kwargs:
            for key, value in kwargs.items():
                if type(value) is int:
                    setattr(self, key, value)
                else:
                    setattr(self, key, 0)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ Compute Perimeter """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Pretty print """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=9, asd="adsf")
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())

    s2 = square(1, True)
    print(s2)
