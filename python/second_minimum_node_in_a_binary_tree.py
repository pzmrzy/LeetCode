# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if node is None:
                return
            if root.val < node.val < res[0]:
                res[0] = node.vals
            dfs(node.left)
            dfs(node.right)
        res = [float('inf')]
        dfs(root)
        return -1 if res[0] == float('inf') else res[0]
