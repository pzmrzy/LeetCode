# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        left = []
        right = []
        if root.left != None:
            left = self.postorderTraversal(root.left)
        if root.right != None:
            right = self.postorderTraversal(root.right)
        return left + right + [root.val]
