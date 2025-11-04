import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

BinTree : TypeAlias = Union[None, "Node"]

@dataclass
class Node:
    val: Any
    left: BinTree
    right: BinTree



@dataclass(frozen=True)
class BinarySearchTree:
    comes_before: Callable[[Any, Any], bool]
    tree: BinTree


#returns False if tree is empty, otherwise returns True
def is_empty(tree: BinarySearchTree) -> bool:
    match tree:
        case None:
            return False
    return True

#adds val to bst in the correct place basses on the comes_before argument of bst
def insert(bst: BinarySearchTree, val: Any) -> BinarySearchTree:

    def insert_helper(bst: BinarySearchTree, func: Callable[[Any, Any], bool], val: Any):
        pass


    return insert_helper(bst, bst.comes_before, val)


