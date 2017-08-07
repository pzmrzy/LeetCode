# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        maxx = max(nums)
        ind = nums.index(maxx)
        res = TreeNode(maxx)
        res.left = self.constructMaximumBinaryTree(nums[:ind])
        res.right = self.constructMaximumBinaryTree(nums[ind + 1:])
        return res
