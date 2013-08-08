__author__ = 'coty'

import unittest
from src.main.Foo import *

class TestFoo(unittest.TestCase):

    def setUp(self):
        print "TestFoo setup."

    def testFoo(self):
        self.foo = Foo(1, 1)

        # these should pass
        assert self.foo.__first__ == 1
        assert self.foo.__second__ == 1

        # this should fail
        assert self.foo.__first__ == 0

if __name__ == "__main__":
    unittest.main()
