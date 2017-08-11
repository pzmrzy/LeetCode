class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        magic = list("1221121221221121122")
        i, j, res = 12, len(magic), 0
        while len(magic) < n:
            if magic[i] == '1':
                if (magic[j - 1] == '1'):
                    magic.append("2")
                else:
                    magic.append("1")
                j += 1
            else:
                if magic[j - 1] == '1':
                    magic.extend(["2", "2"])
                else:
                    magic.extend(["1", "1"])
                j += 2
            i += 1
        for i in range(n):
            if magic[i] == '1':
                res += 1
        return res
