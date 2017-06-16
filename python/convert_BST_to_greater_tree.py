# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root):
        if root is None:
            return
        node = TreeNode(root.val)
        node.right = self.dfs(root.right)
        node.val += self.ct
        self.ct += root.val
        node.left = self.dfs(root.left)
        return node
        
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.ct = 0
        return self.dfs(root)
