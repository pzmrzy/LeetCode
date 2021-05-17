# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorder(self, root, ct):
        if root.left is not None:
            self.inorder(root.left, ct)
        ct[0] -= 1
        if ct[0] == 0:
            ct.append(root.val)
            return
        if root.right is not None:
            self.inorder(root.right, ct)
        
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        ct = [k]
        self.inorder(root, ct)
        return ct[1]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        if root == None:
            return []
        left = []
        right = []
        if root.left != None:
            left = self.inorderTraversal(root.left)
        if root.right != None:
            right = self.inorderTraversal(root.right)
        return left + [root.val] + right
        
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        return self.inorderTraversal(root)[k-1]

