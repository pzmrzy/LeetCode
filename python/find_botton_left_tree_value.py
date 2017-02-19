# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def find(self, root, level):
        self.max = max(self.max, level)
        if (root.right is not None):
            self.find(root.right, level + 1)
        self.dic[level] = root.val
        if (root.left is not None):
            self.find(root.left, level + 1)
        
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dic = {}
        self.max = 0
        self.find(root, 0)
        return self.dic[self.max]
