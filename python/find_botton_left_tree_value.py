# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def find(self, root, level):
        if self.level < level:
            self.level = level
            self.max = root.val
        if (root.left is not None):
            self.find(root.left, level + 1)
        if (root.right is not None):
            self.find(root.right, level + 1)
        
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.level = 0
        self.max = 0
        self.find(root, 1)
        return self.max
