# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def gen(self, l, r):
        ret = []
        if l > r:
            return [None]
        if l == r:
            return [TreeNode(l)]
        for i in range(l, r + 1):
            left = self.gen(l, i - 1)
            right = self.gen(i + 1, r)
            for lnode in left:
                for rnode in right:
                    root = TreeNode(i)
                    root.left = lnode
                    root.right = rnode
                    ret.append(root)
        return ret
    
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.gen(1, n)
