# -------------HackerRank 30 days challenge-------------
# -------------Day08: Dictionaries and Maps-------------

# Read input from STDIN. Print output to STDOUT.

import sys

n = int(sys.stdin.readline().strip())

# Create an empty dictionary.
phone_book = {}

# Step 1: Fill the dictionary.
for _ in range(n):
    entry = sys.stdin.readline().strip().split()
    name = entry[0]
    phone = entry[1]
    phone_book[name] = phone

# Step 2: Query the dictionary.
for line in sys.stdin:
    query_name = line.strip()
    if not query_name:
       break

    if query_name in phone_book:
       print(f"{query_name} = {phone_book[query_name]}")
    else:
       print("Not found")
