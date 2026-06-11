# --------------HackerRank 30 days challenge---------------
# --------------Day 22: Stumped on Binart Search Trees------------

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

    def getHeight(self, root):
        # write your code here
        if root is None:
           return -1
        # Base case: An empty spot has height -1
        # Recursive calls: Go down the left and right paths
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        # Return the maximum of the two heights +1 for the current node
        return max(left_height, right_height) + 1

T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height) 
