class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if len(s) == 0:
            return None
        pos = 1
        ct = 0
        try:
            t = int(s)
            return TreeNode(t)
        except:
            pass
        for pos in range(1, len(s)):
            if s[pos] == '(':
                ct += 1
            elif s[pos] == ')':
                ct -= 1
                if ct == 0:
                    break
        pos1 = 0
        for pos1 in range(0, len(s)):
            if s[pos1] == '(':
                break
        root = TreeNode(int(s[0:pos1]))
        root.left = self.str2tree(s[pos1+1: pos])
        root.right = self.str2tree(s[pos+2:-1])
        return root
