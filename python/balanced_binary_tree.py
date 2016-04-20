# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def height(self, root):
        if root == None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        hl = self.height(root.left)
        hr = self.height(root.right)
        if ((hl - hr == 1) or (hr - hl == 1) or (hr == hl)) and (self.isBalanced(root.left) and self.isBalanced(root.right)):
            return True
        else:
            return False
