# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        def dfs(root):
            if root is None:
                return root
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            if root.val < L:
                return root.right
            if root.val > R:
                return root.left
            return root
        return dfs(root)
