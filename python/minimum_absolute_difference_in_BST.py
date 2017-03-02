# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    res = sys.maxint
    pre = None
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return self.res
        self.getMinimumDifference(root.left)
        if self.pre is not None:
            self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
        self.getMinimumDifference(root.right)
        return self.res
