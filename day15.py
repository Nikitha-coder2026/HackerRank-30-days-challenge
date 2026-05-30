# -------------HackerRank 30 days challenge---------------
# -------------Day 15: Linked Lists-----------------------

class Node:
     def __init__(self, data):
          self.data = data
          self.next = None

class Solution:
     def display(self, head):
         current = head
         while current:
              print(current.data, end = '')
              current = current.next
     def insert(self, head, data):
         # Complete this method
         # 1. Create new node with the data
         new_node = Node(data)
         # 2. If the list is empty, the new node becomes the head
         if head is None:
            return new_node
         # 3. Otherwise walk to the end of the list
         current = head
         while current.next:
               current = current.next
         # 4. Link the last node to our new node
         current.next = new_node
         return head

mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head);
