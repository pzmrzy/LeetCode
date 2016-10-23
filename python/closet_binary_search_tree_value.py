import sys
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def traversal(self, root, target):
        if root == None:
            return
        tmp = abs(target - root.val)
        if tmp < self.dif:
            self.dif = tmp
            self.res = root.val
            
        if root.val > target:
            self.traversal(root.left, target)
        else:
            self.traversal(root.right, target)
        
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.dif = sys.maxint
        self.res = 0
        self.traversal(root, target)
        return self.res
