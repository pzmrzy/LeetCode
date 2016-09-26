class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        if num < 0:
            num += 2 ** 32
        hexl = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
        res = ""
        while num >0:
            res = hexl[num % 16] + res
            num /=16
        return res
