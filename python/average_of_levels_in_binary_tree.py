# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorder(self, root, level):
        if root is None:
            return
        self.dic[level].append(root.val)
        self.preorder(root.left, level + 1)
        self.preorder(root.right, level + 1)
        
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        self.dic = collections.defaultdict(lambda: [])
        self.preorder(root, 0)
        return [float(sum(self.dic[i])) / len(self.dic[i]) for i in sorted(self.dic.keys())]
