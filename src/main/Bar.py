__author__ = 'coty'

class Bar():

    def __init__(self, first, second):
        self.__first__ = first
        self.__second__ = second

    def multiply(self):
        return self.__first__ * self.__second__

    def divide(self):
        return self.__first__ / self.__second__

if __name__ == "__main__":
    b = Bar(1, 1)

    res = b.multiply()
    print "Multiply Result: %i" % res

    res = b.divide()
    print "Divide Result: %i" % res
