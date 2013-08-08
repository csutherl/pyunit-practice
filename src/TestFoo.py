__author__ = 'coty'

import unittest
from Foo import Foo

class TestFoo(unittest.TestCase):

    def testFoo(self):
        f = Foo(1, 1)
        # these should pass
        assert f.__first__ == 1
        assert f.__second__ == 1

        # this should fail
        assert f.__first__ == 0