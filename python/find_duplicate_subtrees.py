# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution(object):
    def preorder(self, root):
        if root is None:
            return '#'
        ret = "%s,%s,%s" % (root.val, self.preorder(root.left), self.preorder(root.right))
        if ret in self.trees and self.trees[ret] == 1:
            self.res.add(root)
            self.trees[ret] == 2
        self.trees[ret] += 1
        return ret
    
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        self.res = set()
        self.trees = defaultdict(lambda: 0)
        self.preorder(root)
        return list(self.res)
