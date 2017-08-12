# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        dic = {}
        def dfs(root):
            if not root:
                return
            dic.setdefault(root.val, 0)
            dic[root.val] += 1
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        maxx = max(dic.values())
        res = []
        for key in dic:
            if dic[key] == maxx:
                res.append(key)
        return res
