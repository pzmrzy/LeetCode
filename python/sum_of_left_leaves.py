# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, lr):
        if root == None:
            return
        if root.left == None and root.right == None and lr == 0:
            self.res += root.val
        if root.left != None:
            self.dfs(root.left, 0)
        if root.right != None:
            self.dfs(root.right, 1)
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 0
        self.res = 0
        if root.left != None:
            self.dfs(root.left, 0)
        if root.right != None:
            self.dfs(root.right, 1)
        return self.res
