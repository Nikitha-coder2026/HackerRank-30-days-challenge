# -------------HackerRank 30 days challenge--------------
# -------------Day 24: More Linked Lists------------

class Node:
     def __init__(self, data):
         self.data = data
         self.next = None

class Solution:
     def insert(self, head, data):
         p = Node(data)
         if head == None:
            head = p
         elif head.next == None:
              head.next = p
         else:
             start = head
             while(start.next!=None):
                   start = start.next
             start.next = p
         return head

     def display(self, head):
         current = head
         while current:
               print(current.data, end = '')
               current = current.next

     def removeDuplicates(self, head):
         # write your code here
         if head == None:
            return None

         current = head
         while current and current.next:
              if current.data == current.next.data:
                 # SKIP the duplicate!
                 current.next = current.next.next
              else:
                 # Move forward only if no duplicate was found
                 current = current.next
         return head

myList = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = myList.insert(head, data)
head = myList.removeDuplicates(head)
myList.display(head)
