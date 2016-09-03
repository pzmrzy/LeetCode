# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        
        l = 0
        r = len(nums)-1
        mid = (l + r) / 2
        root = TreeNode(nums[mid])
        
        if mid - 1 >= l:
            root.left = self.sortedArrayToBST(nums[:mid])
        else:
            root.left = None
        if mid + 1 <= r:
            root.right = self.sortedArrayToBST(nums[mid+1:])
        else:
            root.right = None
        return root
