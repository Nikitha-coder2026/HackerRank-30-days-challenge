# -------------HackerRank 30 days challenge------------
# -------------Day 10: Binary Numbers------------------

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    # Converts number '0b11101' like  str 
    binary_str = bin(n) [2:]
    # we split by '0' to get groups of 1's.
    # '1101' split('0') becomes  ['11','1']
    groups_of_ones = binary_str.split('0')

# Find the length of the longest group.
print(max(len(group) for group in groups_of_ones))
