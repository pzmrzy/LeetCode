# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import Queue
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        q = Queue.Queue()
        q.put((root,root.val,[root.val]))
        ans = []
        while not q.empty():
            now, s, path = q.get()
            if now.left == None and now.right == None:
                if s == sum:
                    ans.append(path)
            if now.left != None:
                q.put((now.left, now.left.val + s, path+[now.left.val]))
            if now.right != None:
                q.put((now.right, now.right.val + s, path+[now.right.val]))
        return ans