# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        if root == None:
            return []
        left = []
        right = []
        if root.left != None:
            left = self.inorderTraversal(root.left)
        if root.right != None:
            right = self.inorderTraversal(root.right)
        return left + [root.val] + right
        
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        return self.inorderTraversal(root)[k-1]

