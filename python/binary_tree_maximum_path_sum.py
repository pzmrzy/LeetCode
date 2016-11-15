class Solution(object):
    def traversal(self, root):
        if root is None:
            return 0
        if self.maxnode < root.val:
            self.maxnode = root.val
        if root.left is None and root.right is None:
            return max(root.val, 0)
        maxpathleft = 0
        maxpathright = 0
        if root.left is not None:
            maxpathleft = self.traversal(root.left)
        if root.right is not None:
            maxpathright = self.traversal(root.right)
        self.res = max([self.res, maxpathleft + maxpathright + root.val])
        return max(max(maxpathleft, maxpathright) + root.val, 0)

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.maxnode = root.val
        if root.left is None and root.right is None:
            return root.val

        self.res = 0
        maxpathleft = 0
        maxpathright = 0
        if root.left is not None:
            maxpathleft = self.traversal(root.left)
        if root.right is not None:
            maxpathright = self.traversal(root.right)
        self.res = max([self.res, maxpathleft + maxpathright + root.val, 0, maxpathleft, maxpathright, self.maxnode])
        if self.maxnode < 0:
            return self.maxnode
        
        return self.res
