class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        res = []
        for it in path.rstrip('/').split('/'):
            if it == '.' or it == "":
                continue
            elif it == "..":
                if len(res) > 0:
                    res.pop()
            else:
                res.append(it)
        return '/' + '/'.join(res)
