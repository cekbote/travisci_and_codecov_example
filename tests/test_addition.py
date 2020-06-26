import unittest
import sys

sys.path.append('..')

from ..src.addition import add


class TestAddition(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 6), 11)
