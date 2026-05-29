# -------------HackerRank 30 days challenge--------------
# ---------------------Day 14: Scope---------------------

class Difference:
     def __init__(self, a):
          self.__elements = a
          # Initialize maximumDifference to 0
          self.maximumDifference = 0
     # The computeDifference method.
     def computeDifference(self):
     # Step 1: Find the largest and smallest numbers
     # This is most efficient way to find the difference gap.
          min_element = min(self.__elements)
          max_element = max(self.__elements)
          self.maximumDifference = abs(min_element - max_element)

_ = input()
a = [int(e) for e in input().split(' ')]
d = Difference(a)
d.computeDifference()
print(d.maximumDifference)
