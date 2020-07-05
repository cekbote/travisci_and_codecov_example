import unittest
import sys
from elasticsearch import Elasticsearch
from travisci_and_codecov_example.src.addition import add, sub


class TestAddition(unittest.TestCase):

    def setUp(self):
        self.es = Elasticsearch()
        self.es.index(index='test', id=1, body={'test': 'test'})
        print(self.es.get(index='test', id=1)['_source'])

    def test_add(self):

        self.assertEqual(add(5, 6), 11)

    def test_sub(self):
        self.assertEqual(sub(6, 5), 1)


if '__name__' == '__main__':
    unittest.main()
