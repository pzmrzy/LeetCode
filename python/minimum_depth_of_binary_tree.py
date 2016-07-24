# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import Queue
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        #if root.left == None and root.right == None:
        #    return 1
        q = Queue.Queue()
        q.put((root,1))
        while True:
            now, depth = q.get()
            if now.left == None and now.right == None:
                return depth
            if now.left != None:
                q.put((now.left, depth+1))
            if now.right != None:
                q.put((now.right, depth+1))