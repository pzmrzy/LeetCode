# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        left = []
        right = []
        if root.left != None:
            left = self.inorderTraversal(root.left)
        if root.right != None:
            right = self.inorderTraversal(root.right)
        return left + [root.val] + right

    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        res = self.inorderTraversal(root)
        target = res.index(p.val) + 1

        if target < len(res):
            f = res[target]
        else:
            return None

        q = [root]
        while len(q) > 0:
            n = q[0]
            del q[0]
            if n.val == f:
                return n
            if n.left != None:
                q.append(n.left)
            if n.right != None:
                q.append(n.right)
