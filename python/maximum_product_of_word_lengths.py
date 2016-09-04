class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dic = {}
        for w in words:
            mask = 0
            for c in w:
                mask |= 1 << (ord(c)-97)
            dic[w] = [mask, len(w)]
        return max([dic[x][1] * dic[y][1] for x in dic for y in dic if dic[x][0] & dic[y][0] == 0 ]+[0])
