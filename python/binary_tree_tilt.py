# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def post(root):
            if root is None:
                return 0
            left = post(root.left)
            right = post(root.right)
            self.res += abs(left - right)
            return left + right + root.val
        post(root)
        return self.res
