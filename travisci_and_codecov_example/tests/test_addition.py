import unittest
import sys
from travisci_and_codecov_example.src.addition import add


class TestAddition(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 6), 13)


if '__name__' == '__main__':
    unittest.main()
