import sys
from typing import TypeAlias, Union, List, Callable
from dataclasses import dataclass
import unittest
sys.setrecursionlimit(10**6)

Llist : TypeAlias = Union["Node", None]

@dataclass(frozen=True)
class Node:
    word: str
    occount: List[int]
    rest: Llist

HashTable : TypeAlias = List[Llist]

# Compute the result of the specified hash function on strings
def hash_fn(s: str) -> int:
    ret=0
    for c in s:
       ret+=ord(c)
    return ret
#Technically not according to spec, for testing only



# Make a fresh hash table with the given size, containing no elements
def make_hash(size: int) -> HashTable:
    return HashTable[size]

# Return the size of the given hash table
def hash_size(ht: HashTable) -> int:
    return len(ht)

# Return the number of elements in the given hash table
def hash_count(ht: HashTable) -> int:
    ret=0
    for c in ht:
       while c != None:
          ret+=1
          c=c.rest
    return ret

# Does the hash table contain a mapping for the given word?
def has_key(ht: HashTable, word: str) -> bool:
    def hasValueinLL(LL: Llist, val: str):
       match LL:
          case None:
             return False
          case Node(w,_,r):
             if w==val:
                return True
             return hasValueinLL(r,val)
    if hasValueinLL(ht[hash_fn(word)],word):
       return True
    return False

# What line numbers is the given key mapped to in the given hash table?
# this list should not contain duplicates, but need not be sorted.
def lookup(ht: HashTable, word: str) -> List[int]:
    def lookupll(LL: Llist, val: str):
       match LL:
          case None:
             raise ValueError("not in list")
          case Node(w,n,r):
             if w==val:
                return n
             return lookupll(r,val)
    if has_key(word):
       return lookupll(ht[hash_fn(word)],word)
    raise ValueError("not in list")

# Add a mapping from the given word to the given line number in
# the given hash table
def add(ht: HashTable, word: str, line: int) -> None:
    def addll(LL: Llist, val: str, line: int):
       match LL:
          case None:
             raise ValueError("not in list")
          case Node(w,n,r):
             if w==val:
                n.append(line)
                return True #just to exit
             return addll(r,val, line)
    if has_key(word):
         return addll(ht[hash_fn(word)],word,line)
    ht[hash_fn(word)] = Node(word, [line], None) if ht[hash_fn(word)]==None else Node(word, [line], ht[hash_fn(word)])

# What are the words that have mappings in this hash table?
# this list should not contain duplicates, but need not be sorted.
def hash_keys(ht: HashTable) -> List[str]:
    def addll(LL: Llist, ret: List[str]):
       match LL:
          case None:
             return True #just to exit
          case Node(w,_,r):
             ret.append(w)
             return addll(r, ret)
    ret=[]
    for ll in ht:
       addll(ll,ret)
    return ret
         

# given a list of stop words and a list of strings representing lines of
# a text, return a hash table
def make_concordance(stop_words: HashTable, text: List[str]) -> HashTable:
  pass

# given an input file , a stop-words file, and an output file, overwrite the output file with
# a sorted concordance of the input file.
def full_concordance(in_file: str, stop_words_file: str, out_file: str) -> None:
  pass



#test cases
class TestCases(unittest.TestCase):
    def sanity(self):
        self.assertTrue(True)
if __name__ == '__main__':
    unittest.main()