# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def check(self, root, num):
        if num > self.res:
            self.res = num
        if root.left != None:
            if root.val + 1 == root.left.val:
                self.check(root.left, num + 1)
            else:
                self.check(root.left, 1)
        if root.right != None:
            if root.val + 1 == root.right.val:
                self.check(root.right, num + 1)
            else:
                self.check(root.right, 1)
        
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.res = 0
        self.check(root, 1)
        return self.res
