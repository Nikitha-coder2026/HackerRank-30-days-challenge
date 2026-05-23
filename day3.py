# -----------HackerRank 30 days challenge-----------
# -----------Day03: Intro to Conditional Statements-----------

import math
import os 
import random
import re
import sys

if __name__ == '__main__':
    N = int(input().strip())

    # Check if N is odd
    if N % 2 != 0:
        print("Weird")
    else:
        # N is even, so check the specific ranges
        if 2 <= N <= 5:
            print("Not Weird")
        elif 6 <= N <= 20:
            print("Weird")
        elif N > 20:
            print("Not Weird")
