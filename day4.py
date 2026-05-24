# -----------HackerRank 30 days challenge-----------
# -----------Day04: Class vs. Instance--------------

class Person:
   def __init__(self, initialAge):
       # Add some more code to run some checks on initialAge
       if initialAge < 0:
           print("Age is not valid, setting age to 0.")
           self.age = 0
       else:
           self.age = initialAge

   def amIOld(self):
       # Do some computations in here and print out the correct statement to console.
       if self.age < 13:
           print("You are young.")
       elif 13 <= self.age < 18:
           print("You are a teenager.")
       else:
           print("You are old.")

   def yearPasses(self):
       # Increement the age of the person in here
       self.age += 1

if __name__ == '__main__':
   t = int(input())
   for i in range(0, t):
       age = int(input())
       p = Person(age)
       p.amIOld()
       for j in range(0, 3):
           p.yearPasses()
       p.amIOld()
       print("")
