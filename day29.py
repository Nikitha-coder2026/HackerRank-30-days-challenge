# -------------HackerRank 30 days challenge-----------------
# ------------------Day 29: Bitwise AND---------------------

import math
import os
import random
import re
import sys

def bitwiseAND(N, k):
    # Write your code here
    if ((k - 1) | k) <= N:
       return k - 1
    return k - 2

if __name__ == '__main__':
   t = int(input().strip())

   for t_itr in range(t):
       first_multiple_input = input().rstrip().split()
       count = int(first_multiple_input[0])
       lim = int(first_multiple_input[1])
       res = bitwiseAND(count, lim)
       print(res)


# ------------------Completed Successfully-------------------
