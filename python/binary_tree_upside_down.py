# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        node, parent, right = root, None, None
        while node is not None:
            left = node.left
            node.left = right
            right = node.right
            node.right = parent
            parent = node
            node = left 
        return parent
        # if root is None:
        #     return
        # parent, left, right = root, root.left, root.right
        # if left is not None:
        #     ret = self.upsideDownBinaryTree(left)
        #     left.left = right
        #     left.right = parent
        #     return ret
        # return root
