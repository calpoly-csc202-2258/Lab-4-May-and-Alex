import sys
import unittest
from typing import *
from dataclasses import dataclass
import math
import matplotlib.pyplot as plt
import numpy as np
import random
sys.setrecursionlimit(10**6)

from bst import *

TREES_PER_RUN : int = 10000

def graph_heights_of_random_trees() -> None:
    # here we're using "list comprehensions": more of Python's
    # syntax sugar.
    x_coords : List[int] = [ int(i) for i in range( 0,  n_max) ]
    y_coords : List[float] = all_heights_avg
    # Could have just used this type from the start, but I want
    # to emphasize that 'matplotlib' uses 'numpy''s specific array
    # type, which is different from the built-in Python array
    # type.
    x_numpy : np.ndarray = np.array( x_coords )
    y_numpy : np.ndarray = np.array( y_coords )
    plt.plot( x_numpy, y_numpy, label = 'Average Height' )
    plt.xlabel("n values in tree")
    plt.ylabel("Height of tree")
    plt.title("Height of Random Trees")
    plt.grid(True)
    plt.legend() # makes the 'label's show up
    plt.show()


if (__name__ == '__main__'):
    graph_heights_of_random_trees()