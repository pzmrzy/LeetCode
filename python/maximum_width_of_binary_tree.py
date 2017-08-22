# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, depth, pos):
            dic[depth][0] = min(dic[depth][0], pos)
            dic[depth][1] = max(dic[depth][1], pos)
            if root.left is not None:
                dfs(root.left, depth + 1, pos * 2)
            if root.right is not None:
                dfs(root.right, depth + 1, pos * 2 + 1)
            
        dic = defaultdict(lambda : [float('inf'), float('-inf')])
        dfs(root, 0, 0)
        return max([r - l + 1 for l, r in dic.values()])
