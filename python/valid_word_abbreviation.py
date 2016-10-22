import string
class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        word += 'a'
        abbr += 'a'
        ind = 0
        flag = True
        buf = 0
        l = len(word)
        for c in abbr:
            if c in string.lowercase:
                if ind >= l:
                        return False
                if flag:
                    if c != word[ind]:
                        return False
                    else:
                        ind += 1
                else:
                    ind += buf
                    buf = 0
                    if ind >= l:
                        return False
                    if c != word[ind]:
                        return False
                    else:
                        ind += 1
                    flag = True
            else:
                if buf == 0 and c == '0':
                    return False
                flag = False
                buf *= 10
                buf += int(c)
        if ind < l:
            return False
        return True
