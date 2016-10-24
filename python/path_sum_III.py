# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def traversal(self, root, sum):
        if root == None:
            return 0
        ret = 0
        if root.val == sum:
            ret += 1
        ret += self.traversal(root.left, sum - root.val)
        ret += self.traversal(root.right, sum - root.val)
        return ret
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root == None:
            return 0
        res = 0
        if root.val == sum:
            res += 1
        res += self.pathSum(root.left, sum)
        res += self.pathSum(root.right, sum)
        res += self.traversal(root.left, sum - root.val)
        res += self.traversal(root.right, sum - root.val)
        return res
