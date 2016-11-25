# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, lev):
        if root.left is not None:
            self.dfs(root.left, lev + 1)
        self.dic.setdefault(lev, [])
        self.dic[lev].append(root.val)
        if root.right is not None:
            self.dfs(root.right, lev + 1)
            
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        self.dic = {}
        self.dfs(root, 0)
        res = []
        for i in range(max(self.dic.keys()) + 1):
            res.append(self.dic[i] if i % 2 == 0 else self.dic[i][::-1])
        
        return res
