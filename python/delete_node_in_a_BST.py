# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            tmp = root.right
            minn = tmp.val
            while tmp.left:
                tmp = tmp.left
                minn = tmp.val
            root.val = minn
            root.right = self.deleteNode(root.right, minn)
        return root
