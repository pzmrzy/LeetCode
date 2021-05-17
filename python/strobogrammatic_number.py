class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        l, r = 0, len(num) - 1
        while l < r:
            if num[l] + num[r] not in {'69', '96', '88', '00', '11'}:
                return False
            l += 1
            r -= 1
        if l == r and num[l] not in '180':
            return False
        return True
class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dic = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6', '2':'#', '3':'#', '4':'#', '5':'#', '7':'#'}
        l = len(num)
        for i in range(l / 2 + 1):
            if dic[num[i]] != num[l - i - 1]:
                return False
        return True
