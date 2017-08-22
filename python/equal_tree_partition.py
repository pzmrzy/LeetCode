# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def sumtree(node):
            if node is None:
                return 0
            tmp = node.val + sumtree(node.left) + sumtree(node.right)
            print tmp
            if node is not root:
                cut.add(tmp)
            return tmp
        cut = set()
        return sumtree(root) / 2. in cut
