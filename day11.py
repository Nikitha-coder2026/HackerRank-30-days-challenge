# -------------HackerRank 30 days challenge------------
# -------------Day 11: 2D Arrays-----------------------

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # initialize max_sum to a very small numbers to handle negative values.
    max_sum = -float('inf')

    # Iterate through possible hourglass starting point
    # Loops stop at range (4) to prevent "Index out of range" error

    for i in range(4):
        for j in range(4):
            # Calculate the current hourglass sum
            Current_sum = (arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
                           + arr[i + 1][j + 1] +
                           arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2])

            # Update max_sum if Current_sum is larger
            if Current_sum > max_sum:
                max_sum = Current_sum

    print(max_sum)
