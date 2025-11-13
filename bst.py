import random
import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)
import time

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

TREES_PER_RUN = 10000


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
                elif func(v,val): #might be in reverse
                    return lookup_helper(l, v, func)
                else:
                    return lookup_helper(r, v, func)
    return lookup_helper(tree.tree,v,tree.comes_before)

#deletes val from tree
def delete(otree: BinarySearchTree, val: Any) -> BinarySearchTree:
    def del_helper (btree: BinTree, val: Any, func: Callable[[Any, Any], bool]) -> BinTree:
        def dellargest(dtree: BinTree) -> BinTree:
            match dtree:
                case None:
                    raise ValueError ("deleted the largest leaf of a nonexistant tree")
                case Node(v, l, r):
                    if r is None:
                        return l
                    return Node(v,l,dellargest(r))
        def largest_val(ltree: BinTree) -> Any:
            match ltree:
                case None:
                    raise ValueError ("tried to find the largest leaf of a nonexistant tree")
                case Node(v, _, r):
                    if r is None:
                        return v
                    return largest_val(r)
        match btree:
            case None:
                return None
            case Node(v, l, r):
                if v==val:
                    return Node(largest_val(l),dellargest(l),r)
                elif func(val,v):
                    return Node(v, del_helper(l,val,func), r)
                else:
                    return Node(v, l, del_helper(r,val,func))
    return BinarySearchTree(otree.comes_before, del_helper(otree.tree, val, otree.comes_before))



def height(btree : BinTree) -> int:
    if btree is None:
        return 0
    return 1 + max(height(btree.left), height(btree.right))

n_max = 30
heights_total = 0
all_heights_avg = []

for i in range(n_max):
    for i in range(TREES_PER_RUN):
        btree = random_tree(n_max)
        heights_total += height(btree.tree)
    heights_total = heights_total / TREES_PER_RUN
    all_heights_avg.append(heights_total)





'''
Make a graph of average tree height (y axis) as a funcƟon of N (x axis). Use 50(do 30) different N
samples spaced evenly from N=0 to N=n_max. At each N you’ll find the average height of
TREES_PER_RUN random trees of size N. 
'''