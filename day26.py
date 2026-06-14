# -------------HackerRank 30 days challenge---------------
# -------------Day 26: Nested Logic-----------------------

# Read the actual return date.
d1, m1, y1 = map(int, input().split())

# Read the expected return date.
d2, m2, y2 = map(int, input().split())

fine = 0

# Check year first(The Biggest Fine)
if y1 > y2:
   fine = 10000
elif y1 == y2:
     # Year is same, check month
     if m1 > m2:
        fine = 500 * (m1 - m2)
     elif m1 == m2:
          # Month is same, check day
          if d1 > d2:
             fine = 15 * (d1 - d2)

# If y1 < y2, fine remains 0(returned in a previous year)
print(fine)
