# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        res = {}
        q = [(root, 0)]
        while len(q) > 0:
            n, pos = q[0]
            del q[0]
            res.setdefault(pos, [])
            res[pos].append(n.val)
            if n.left != None:
                q.append( (n.left, pos - 1) )
            if n.right != None:
                q.append( (n.right, pos + 1) )
                
        keys = res.keys()
        minn = min(keys)
        maxx = max(keys)
        
        ret = []
        for i in range(minn, maxx + 1):
            ret.append(res[i])
        return ret
