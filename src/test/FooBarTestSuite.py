__author__ = 'coty'

import unittest

from src.test.TestFoo import *
from src.test.TestBar import *

FooBarTestSuite = unittest.TestSuite()
FooBarTestSuite.addTest(TestFoo("testFoo"))
FooBarTestSuite.addTest(TestBar("testBar"))

if __name__ == "__main__":
    unittest.main()
