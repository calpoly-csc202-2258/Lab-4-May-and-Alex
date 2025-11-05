import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)
from bst import *

class BSTTests(unittest.TestCase):
    #insert
    def test_insert1(self):
        og_bst = BinarySearchTree(comes_before_lessthan, Node(5,
                                                         left =  Node(3,
                                                                      left = Node(2, None, None),
                                                                      right = Node(4, None, None)),
                                                         right = Node(7, None, None)))

        expected_bst = BinarySearchTree(comes_before_lessthan, Node(5,
                                                         left =  Node(3,
                                                                      left = Node(2, None, None),
                                                                      right = Node(4, None, None)),
                                                         right = Node(7,
                                                                      left = Node(6, None, None),
                                                                      right = None)))
        self.assertEqual(insert(og_bst, 6), expected_bst)

    def test_insert2(self):
        og_bst = BinarySearchTree(comes_before_lessthan, Node(5,
                                                         left =  Node(3, None, None),
                                                         right = Node(7, None, None)))

        expected_bst = BinarySearchTree(comes_before_lessthan, Node(5,
                                                         left =  Node(3, None, None),
                                                         right = Node(7, None, None)))
        self.assertEqual(insert(og_bst, 7), expected_bst)

    #idk how to make test functions for random_tree

    def test_example(self):
        pass


if (__name__ == '__main__'):
 unittest.main()
