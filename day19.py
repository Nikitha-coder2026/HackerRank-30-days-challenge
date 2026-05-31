# -------------HackerRank 30 days challenge--------------
# ----------Day 19: Interacting with Interfaces------------

# Building knowledge of Abstraction with this Interfaces Challenges

class AdvancedArithmetic(object):
      def divisorSum(n):
          raise NotImplementedError

# This is your part of the challenge!
class Calculator(AdvancedArithmetic):
      def divisorSum(self, n):
          pass
          total_sum = 0
          # We loop from 1 to n to find every number that divides n perfectly.
          for i in range(1, n + 1):
              if n % i == 0:
                 total_sum += i
          return total_sum

# Testing code
n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implement: " + type(my_calculator).__bases__[0].__name__)
print(s)
