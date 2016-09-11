# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorder(self, root, lev):
        if root == None:
            return []
        left = []
        right = []
        if root.left != None:
            left = self.inorder(root.left, lev+1)
        if root.right != None:
            right = self.inorder(root.right, lev+1)
        return left + [(root.val, lev)] + right
        
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        inord = self.inorder(root, 0)
        t = {}
        for x, y in inord:
            t[y] = x
        res = []
        for i in range(len(t)):
            res.append(t[i])
        return res
