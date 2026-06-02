# -------------HackerRank 30 days challenge--------------
# ---------------------Day 20: Sorting-------------------

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    
    # Write Your Code Here
    total_swaps = 0

    for i in range(n):
        for j in range(n - 1):
            # Swap if elements are in wrong order
            if a[j] > a[j + 1]:
               a[j], a[j + 1] = a[j + 1], a[j]
               total_swaps += 1
            # Optimization: If no swaps happened in a round, its already sorted!
            if total_swaps == 0:
               break
    print(f"Array is sorted in {total_swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
