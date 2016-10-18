# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def build(self, ini, inj, posti, postj):
        if ini - inj == 0:
            return None
        rootval = self.postorder[posti: postj][-1]
        ind = self.inorder[ini: inj].index(rootval)
        res = TreeNode(rootval)

        leftin1 = ini
        rightin1 = ini + ind
        leftpost1 = posti
        rightpost1 = posti + ind

        leftin2 = rightin1 + 1
        rightin2 = inj
        leftpost2 = rightpost1
        rightpost2 = postj - 1

        if rightin1 - leftin1 != 0:
            res.left = self.build(leftin1, rightin1, leftpost1, rightpost1)

        if rightin2 - leftin2 != 0:
            res.right = self.build(leftin2, rightin2, leftpost2, rightpost2)
        return res

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.inorder = inorder
        self.postorder = postorder
        del inorder
        del postorder
        return self.build(0, len(self.inorder), 0, len(self.postorder))
