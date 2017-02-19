# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys
class Solution(object):
    def find(self, root, lev):
        self.dic.setdefault(lev, -sys.maxint)
        self.lev = max(self.lev, lev)
        self.dic[lev] = max(root.val, self.dic[lev])
        if (root.left is not None):
            self.find(root.left, lev + 1)
        if (root.right is not None):
            self.find(root.right, lev + 1)
            
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        self.lev = 0
        self.dic = {}
        self.find(root, 0)
        res = []
        for i in range(self.lev + 1):
            res.append(self.dic[i])
        return res
