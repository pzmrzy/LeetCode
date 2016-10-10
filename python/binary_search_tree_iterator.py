mport Queue
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
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
        
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        #self.q = Queue.Queue()
        self.t = self.inorderTraversal(root)
        self.n = len(self.t) - 1
        self.now = -1
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.now < self.n

    def next(self):
        """
        :rtype: int
        """
        self.now += 1
        return self.t[self.now]
        
# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
