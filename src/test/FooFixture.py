__author__ = 'coty'

import unittest
# from src.main.Foo import *
# from src.test.TestFoo import *

class FooFixture(unittest.TestCase):
    def setup(self):
        print "Fixture setup."

if __name__ == "__main__":
    # print TestFoo.__bases__
    # exec "TestFoo.__bases__ = (FooFixture,)"
    # print TestFoo.__bases__
    unittest.main()