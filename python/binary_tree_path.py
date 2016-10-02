import Queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def find(self, root, path):
        path.append(root.val)
        if root.left == root.right == None:
            self.res.append(path)
            return
        if root.left != None:
            self.find(root.left, path[:])
        if root.right != None:
            self.find(root.right, path[:])
            
    def binaryTreePaths(self, root):
        if root == None:
            return []
        if root.left == root.right == None:
            return [str(root.val)]
        self.res = []
        self.find(root, [])
        res = []
        for v in self.res:
            res.append('->'.join(map(str, v)))
        return res
