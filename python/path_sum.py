# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import Queue
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        q = Queue.Queue()
        q.put((root,root.val))
        while not q.empty():
            now, s = q.get()
            if now.left == None and now.right == None:
                if s == sum:
                    return True
            if now.left != None:
                q.put((now.left, now.left.val + s))
            if now.right != None:
                q.put((now.right, now.right.val + s))
        return False