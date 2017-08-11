# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if not root:
            return [""]
        def dep(root):
            if not root:
                return 0
            return max(dep(root.left), dep(root.right)) + 1
        depth = dep(root)
        res = [[""] * (2 ** depth - 1) for _ in range(depth)]
        
        def fill(root, d, pos):
            res[-d][pos] = str(root.val)
            if root.left:
                fill(root.left, d - 1, pos - 2 ** (d - 2))
            if root.right:
                fill(root.right, d - 1, pos + 2 ** (d - 2))
            
        fill(root, depth, 2 ** (depth - 1) - 1)
        return res
