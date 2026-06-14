# -------------HackerRank 30 days challenge-------------
# -------------Day 25: Running Time and Complexity------------

import math

def is_prime(n):
    if n <= 1:
       return False
    if n <= 3:
       return True
    if n % 2 == 0 or n % 3 == 0:
       return False

    # We only check up to the square root of n.
    # This turns a slow O(n) task into a fast O(sqrt(n))
    
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
           return False
    return True

# Reading input
t = int(input()) # The number of test cases

for _ in range(t):
    n = int(input())
    if is_prime(n):
       print("prime")
    else:
       print("Not prime")
