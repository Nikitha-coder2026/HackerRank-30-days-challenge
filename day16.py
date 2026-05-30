# -------------HavkerRank 30 days challenge---------------
# --------Day 16: Exceptions - String to Integer----------

#!/bin/python3

S = input().strip()
try:
    result = int(S)
    print(result)
except ValueError:
      print("Bad String")

