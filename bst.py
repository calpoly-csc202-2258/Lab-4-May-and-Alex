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