__author__ = 'coty'

class Foo():

    def __init__(self, first, second):
        self.__first__ = first
        self.__second__ = second

    def add(self):
        return self.__first__ + self.__second__

    def subtract(self):
        return self.__first__ - self.__second__

if __name__ == "__main__":
    f = Foo(1, 1)
    res = f.add()
    print "Add Result: %i" % res
    res = f.subtract()
    print "Subtract Result: %i" % res
