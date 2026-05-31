# -------------HackerRank 30 days challenge---------------
# ----------------Day 18: Queues And Stacks---------------

import sys

class Solution:
     def __init__(self):
          # Initialize our two containers
          self.stack = []
          self.queue = []

     # Stack: Push to the end
     def pushCharacter(self, char):
         self.stack.append(char)

     # Queues: Enqueue to the end
     def enqueueCharacter(self, char):
         self.queue.append(char)

     # Stack: Pop from the end(LIFO)
     def popCharacter(self):
         return self.stack.pop()

     # Queues: Dequeue from the front(FIFO)
     def dequeueCharacter(self):
         return self.queue.pop(0)

# Read the string s
s = input()

# Create the solution class object
obj = Solution()

l = len(s)
# Push|enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True

'''
pop the top character from stack dequeue the first character from queue
Compare both the characters
'''

for i in range(l//2):
    if obj.popCharacter() != obj.dequeueCharacter():
       isPalindrome = False
       break

# Finally print whether string s is palindrome or not.
if isPalindrome:
     print("The word, "+s+", is a palindrome.")
else:
     print("The word, "+s+", is not a palindrome.")
