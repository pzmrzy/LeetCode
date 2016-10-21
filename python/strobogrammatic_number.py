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
