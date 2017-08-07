# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Queue import Queue
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        nums = set()
        q = Queue()
        q.put(root)
        while not q.empty():
            now = q.get()
            if now is None:
                continue
            if (k - now.val) in nums:
                return True
            nums.add(now.val)
            if now.left is not None:
                q.put(now.left)
            if now.right is not None:
                q.put(now.right)
        return False
