class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic = {}
        for c in magazine:
            dic.setdefault(c, 0)
            dic[c] += 1
            
        for c in ransomNote:
            dic.setdefault(c, 0)
            if dic[c] == 0:
                return False
            else:
                dic[c] -= 1
                
        return True
