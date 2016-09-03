# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        left = []
        right = []
        if root.left != None:
            left = self.inorderTraversal(root.left)
        if root.right != None:
            right = self.inorderTraversal(root.right)
        return left + [root.val] + right
