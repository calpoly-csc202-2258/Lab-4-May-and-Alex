import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

BinTree : TypeAlias = Union[None, "Node"]

@dataclass(frozen=True)
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

def comes_before_test(new: float, old: float)-> bool:
    if new > old:
        return True
    else:
        return False

#adds val to bst in the correct place basses on the comes_before argument of bst
def insert(bst: BinarySearchTree, val: Any) -> BinarySearchTree:

    def insert_helper(bst: BinarySearchTree, func: Callable[[Any, Any], bool], new_val: Any):
        match bst:
            case None:
                return Node(new_val, None, None)
            case Node(v, l, r):
                if new_val == v:
                    return Node

                if func(new_val, v) is True:
                    return insert_helper(l, func, new_val)
                else:
                    return insert_helper(r, func, new_val)

    return insert_helper(bst, bst.comes_before, val)





