import random
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
    match tree.tree:
        case None:
            return False
    return True

def comes_before_lessthan (new: float, old: float)-> bool:
    if new < old:
        return True
    else:
        return False

#adds val to given_bst in the correct place basses on the comes_before argument of given_bst
def insert(given_bst: BinarySearchTree, val: Any) -> BinarySearchTree:

    def insert_helper(bst: Node, func: Callable[[Any, Any], bool], new_val: Any):
        match bst:
            case None:
                return Node(new_val, None, None)

            case Node(v, l, r):
                if new_val == v:
                    return Node(v, l, r)

                if func(new_val, v) is True:
                    return Node(v, insert_helper(l, func, new_val), r)
                else:
                    return Node(v, l, insert_helper(r, func, new_val))

    return BinarySearchTree(given_bst.comes_before, insert_helper(given_bst.tree, given_bst.comes_before, val))

#returns a random BinarySearchTree composed of 'n' random floats [0,1]
def random_tree(n: int)-> BinarySearchTree:

    tree : BinarySearchTree = BinarySearchTree(comes_before_lessthan, None)

    for numb in range(n):
        tree = insert(tree, random.random())

    return tree


#returns True if v is in tree, otherwise returns False
def lookup(tree: BinarySearchTree, v: Any) -> bool:
    def lookup_helper(tree: BinTree, v: Any, func: Callable[[Any, Any], bool]) -> bool:
        match tree:
            case None:
                return False
            case Node(val,l,r):
                if v==val:
                    return True
                elif func(v,val): #might be reverse
                    return lookup_helper(l, v, func)
                else:
                    return lookup_helper(r, v, func)
    return lookup_helper(tree.tree,v,tree.comes_before)

