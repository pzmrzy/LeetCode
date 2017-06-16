# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
class Solution(object):
    def dfs(self, root):
        if root is None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        tmp = root.val + left + right
        self.dic[tmp] += 1
        return tmp
        
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        self.dic = defaultdict(lambda: 0)
        self.dfs(root)
        maxv = max(self.dic.values())
        res = []
        for k, v in self.dic.items():
            if v == maxv:
                res.append(k)
        return res
