import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

BST : TypeAlias = Union[None, "BSTNode"]

@dataclass(frozen=True)
class BSTNode:
    val: Any
    left: BST
    right: BST

    comes_before: Callable[[Any,Any],bool]