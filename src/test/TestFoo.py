__author__ = 'coty'

import unittest
from src.main.Foo import *
from src.test.FooFixture import *

# class TestFoo(unittest.TestCast):
class TestFoo(FooFixture):

    # def setUp(self):
    #     print "TestFoo setup."

    # def testFoo(self):
    def runTest(self):
        self.foo = Foo(1, 1)

        # these should pass
        assert self.foo.__first__ == 1
        assert self.foo.__second__ == 1

        # this should fail
        assert self.foo.__first__ == 0

if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFoo)
    t = unittest.TextTestRunner(verbosity=2).run(suite)
    print t