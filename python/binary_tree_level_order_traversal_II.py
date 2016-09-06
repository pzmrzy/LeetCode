# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def traversal(self, root, n):
        self.res.setdefault(n, [])
        self.res[n].append(root.val)
        if root.left != None:
            self.traversal(root.left, n + 1)
        if root.right != None:
            self.traversal(root.right, n + 1)
        
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        self.res = {}
        self.res[0]=[root.val]
        self.traversal(root, 1)
        return self.res
