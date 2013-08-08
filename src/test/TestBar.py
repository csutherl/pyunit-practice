__author__ = 'coty'

import unittest
from src.main.Bar import *

class TestBar(unittest.TestCase):

    def testBar(self):
        b = Bar(1, 1)
        # these should pass
        assert b.__first__ == 1
        assert b.__second__ == 1

        # this should fail
        assert b.__first__ == 0

if __name__ == "__main__":
    unittest.main()
