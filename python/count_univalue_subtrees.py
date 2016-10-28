# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def traversal(self, root):
        if root is None:
            return 0, True, None
        if root.left is None and root.right is None:
            return 1, True, root.val
        cntl, flagl, numl = self.traversal(root.left)
        cntr, flagr, numr = self.traversal(root.right)
        X = (cntl + cntr + 1, True, root.val)
        Y = (cntl + cntr, False, root.val)
        if flagl and flagr:
            if numl is None:
                if numr == root.val:
                    return X
                else:
                    return Y
            elif numr is None:
                if numl == root.val:
                    return X
                else:
                    return Y
            else:
                if root.val == numl == numr:
                    return X
                else:
                    return Y
        else:
            return Y

    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return self.traversal(root)[0]
