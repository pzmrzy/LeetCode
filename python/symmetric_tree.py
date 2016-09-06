# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def chk(self, left, right):
        if left != None and right == None:
            return False
        if left == None and right != None:
            return False
        if left == None and right == None:
            return True
        if left.val != right.val:
            return False
        
        return self.chk(left.left, right.right) and self.chk(left.right, right.left)
        
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.chk(root.left, root.right)
