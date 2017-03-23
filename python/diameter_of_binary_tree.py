# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    res = 0
    def dfs(self, root):
        if root is None:
            return 0
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        self.res = max(self.res, l + r)
        return max(l, r) + 1
        
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.res
