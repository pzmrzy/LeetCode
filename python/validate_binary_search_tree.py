# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def check(self, root, l, r):
        if root == None:
            return True
        if root.val <= l or root.val >= r:
            return False
        if root.left != None:
            if root.left.val >= root.val:
                return False
        if root.right != None:
            if root.right.val <= root.val:
                return False
        return self.check(root.left, l, root.val) and self.check(root.right, root.val, r)
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.check(root.left, -sys.maxint, root.val) and self.check(root.right, root.val, sys.maxint)
