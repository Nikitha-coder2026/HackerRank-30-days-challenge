# --------------HackerRank 30 days challenge-------------
# --------------Day 23: BST Level-Order Traversal-------------

import sys

class Node:
     def __init__(self, data):
          self.right = self.left = None
          self.data = data

class Solution:
     def insert(self, root, data):
         if root == None:
            return Node(data)
         else:
            if data <= root.data:
               cur = self.insert(root.left, data)
               root.left = cur
            else:
               cur = self.insert(root.right, data)
               root.right = cur
            return root

     def levelOrder(self, root):
         # write your code here
         if root is None:
            return
         # Initialize our 'Queue' with the root.
         queue = [root]

         while len(queue) > 0:
              # Pop the first element (the front of the line).
              node = queue.pop(0)

              # Print the data (end = " " keeps it on one line)
              print(node.data, end = "")

              # Add children to the back of the line.
              if node.left:
                 queue.append(node.left)

              if node.right:
                 queue.append(node.right)

T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)
