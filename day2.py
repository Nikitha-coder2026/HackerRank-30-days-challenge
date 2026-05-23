# -----------HackerRank 30 days challenge-------------
# -----------Day02: Operators-------------

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters: 
# 1. Double meal_cost
# 2. Integer tip_percent
# 3. Integer tax_ percent
#

def solve(meal_cost, tip_percent, tax_percent):
     # Calculate the tip amount using math operators
     tip = meal_cost * (tip_percent / 100)
     # Calculate the tax amount using math operators
     tax = meal_cost * (tax_percent / 100)
     # Add them all up to get the total cost
     total_cost = meal_cost + tip + tax
     # Use Python's built-in round() function to get the nearest integer
     print(round(total_cost))

if --name-- == '--main--':
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
