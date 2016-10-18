# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def build(self, ini, inj, prei, prej):
        if ini - inj == 0:
            return None
        rootval = self.preorder[prei: prej][0]
        ind = self.inorder[ini: inj].index(rootval)
        res = TreeNode(rootval)

        leftin1 = ini
        rightin1 = ini + ind
        leftpre1 = prei + 1#posti
        rightpre1 = prei + 1 + ind#posti + ind

        leftin2 = rightin1 + 1
        rightin2 = inj
        leftpre2 = rightpre1#rightpost1
        rightpre2 = prej#postj - 1

        if rightin1 - leftin1 != 0:
            res.left = self.build(leftin1, rightin1, leftpre1, rightpre1)

        if rightin2 - leftin2 != 0:
            res.right = self.build(leftin2, rightin2, leftpre2, rightpre2)
        return res

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.inorder = inorder
        self.preorder = preorder
        return self.build(0, len(self.inorder), 0, len(self.preorder))
