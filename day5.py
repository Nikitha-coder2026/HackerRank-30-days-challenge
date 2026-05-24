# ------------HackerRank 30 days challenge------------
# ------------Day05: Loops----------------

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    # Loop from 1 to 10 inclusive.
    for i in range(1, 11):
        # Calculate the result
        result = n * i
        # Print using a clean f-string formatting
        print(f"{n} X {i} = {n * i}")
