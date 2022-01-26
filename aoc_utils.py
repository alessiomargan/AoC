# ### IMPORTS
import os
import urllib.request

import re
import numpy as np
import math
import random
import time
import string
from typing      import Generator, Iterator, Iterable
from collections import Counter, defaultdict, namedtuple, deque, abc, OrderedDict, ChainMap
from functools   import lru_cache
from statistics  import mean, median, mode, stdev, variance
from itertools   import (permutations, combinations, chain, cycle, product, islice,
                         takewhile, zip_longest, count as count_from, tee, pairwise)
from more_itertools import partition, sliding_window, nth, grouper
from heapq import heappop, heappush
#from numba import jit
from dataclasses import dataclass
from aocd import get_data, submit

# ### CONSTANTS

infinity = float('inf')
bignum = 10 ** 100


# ### FILE INPUT AND PARSING

def get_in_file(day):
    with open( f"input/input{day}.txt", "w") as f:
        f.write( get_data(day=day, year=2021) )

def parse(day, parser=str, sep='\n') -> tuple:
    """Split the day's input file into entries separated by `sep`, and apply `parser` to each."""
    entries = open(f'input/input{day}.txt').read().rstrip().split(sep)
    return mapt(parser, entries)
    
def Input(day, line_parser=str.strip, file_template='input/input{}.txt'):
    "For this day's input file, return a tuple of each line parsed by `line_parser`."
    return mapt(line_parser, open(file_template.format(day)))

def ints(text):
    "A tuple of all integers in a string (ignore other characters)."
    return mapt(int, re.findall(r'-?[0-9]+', text))


# ### UTILITY FUNCTIONS

def mapt(fn, *args):
    "Do a map, and make the results into a tuple."
    return tuple(map(fn, *args))

def upto(iterable, maxval):
    "From a monotonically increasing iterable, generate all the values <= maxval."
    # Why <= maxval rather than < maxval? In part because that's how Ruby's upto does it.
    return takewhile(lambda x: x <= maxval, iterable)

#T = TypeVar('T')
#def chunks(iterator: Iterator[T], n: int) -> Iterator[Iterator[T]]:
#    return (chain([first], islice(iterator, 0, n - 1)) for first in iterator)

def chunks(iterable, n):
    it = iter(iterable)
    while True:
        chunk = tuple(islice(it, n))
        if not chunk:
            return
        yield chunk


def get_adj_cross(i,j,M):
    """
          | i-1,j |
    ------------------------
    i,j-1 | i  ,j | i,j+1
    ------------------------
          | i+1,j |  
    """
    I,J = M.shape
    I -= 1
    J -= 1
    adj = dict()
    if i > 0:
        adj[(i-1,j)] = M[i-1,j]
    if i < I:
        adj[(i+1,j)] = M[i+1,j]
    if j > 0:
        adj[(i,j-1)] = M[i,j-1]
    if j < J:
        adj[(i,j+1)] = M[i,j+1]
    return adj


def get_adj(i,j,M,diag=True) -> dict :
    """
     i-1,j-1 | i-1,j | i-1,j+1
    --------------------------
       i,j-1 | i , j |   i,j+1
    --------------------------
     i+1,j-1 | i+1,j | i+1,j+1  
    """
    I,J = M.shape
    rangeI = range(I)
    rangeJ = range(J)
    adj = dict()
    exclude = set([(0,0)])
    if not diag :
        exclude |= set([(-1,-1),(-1,1),(1,1),(1,-1)])
    for (di,dj) in product(range(-1,2),repeat=2) :
        _i,_j = i+di,j+dj  
        if ( _i in rangeI and _j in rangeJ and (di,dj) not in exclude ):
            adj[(_i,_j)] = M[_i,_j]
    return adj
