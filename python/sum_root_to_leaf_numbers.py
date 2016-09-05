# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    res = 0
    def find(self, root, n):
        now = n + root.val
        f = True
        if root.left != None:
            self.find(root.left, now * 10)
            f = False
        if root.right != None:
            self.find(root.right, now * 10)
            f = False
        if f:
            print now
            self.res += now
        
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.find(root, 0)
        return self.res
