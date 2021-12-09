# ### IMPORTS
import os
import urllib.request

import re
import numpy as np
import math
import random
import time
import string

from collections import Counter, defaultdict, namedtuple, deque, abc, OrderedDict
from functools import lru_cache
from statistics import mean, median, mode, stdev, variance
from itertools import (permutations, combinations, chain, cycle, product, islice,
                       takewhile, zip_longest, count as count_from, tee, pairwise)
from more_itertools import partition
from heapq import heappop, heappush
#from numba import jit
from dataclasses import dataclass

# ### CONSTANTS

infinity = float('inf')
bignum = 10 ** 100


# ### FILE INPUT AND PARSING


def Input(day, line_parser=str.strip, file_template='input/input{}.txt'):
    "For this day's input file, return a tuple of each line parsed by `line_parser`."
    return mapt(line_parser, open(file_template.format(day)))


def integers(text):
    "A tuple of all integers in a string (ignore other characters)."
    return mapt(int, re.findall(r'-?\d+', text))


# ### UTILITY FUNCTIONS


def mapt(fn, *args):
    "Do a map, and make the results into a tuple."
    return tuple(map(fn, *args))


def first(iterable, default=None):
    "Return first item in iterable, or default."
    return next(iter(iterable), default)


def nth(iterable, n, default=None):
    "Returns the nth item of iterable, or a default value"
    return next(islice(iterable, n, None), default)


def upto(iterable, maxval):
    "From a monotonically increasing iterable, generate all the values <= maxval."
    # Why <= maxval rather than < maxval? In part because that's how Ruby's upto does it.
    return takewhile(lambda x: x <= maxval, iterable)
