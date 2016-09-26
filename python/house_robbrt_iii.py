# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dp(self, root):
        if root == None:
            return 0
        t1 = root.val
        if t1 < 0:
            return -t1
        if root.left != None:
            t1 += self.dp(root.left.left) + self.dp(root.left.right)
        if root.right != None:
            t1 += self.dp(root.right.left) + self.dp(root.right.right)
        t2 = self.dp(root.left) + self.dp(root.right)
        root.val = -max(t1, t2)
        return -root.val
        
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dp(root)
