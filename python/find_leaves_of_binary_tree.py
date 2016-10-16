# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def find(self, root):
        if root == None:
            return 0
        left = self.find(root.left)
        right = self.find(root.right)
        lev = max(left, right) + 1
        self.dic.setdefault(lev, [])
        self.dic[lev].append(root.val)
        return lev
        
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.dic = {}
        self.res = []
        self.find(root)
        res = []
        for i in range(1, len(self.dic) + 1):
            res.append(self.dic[i])
        return res
