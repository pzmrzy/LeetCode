import Queue
class Solution(object):
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
        
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        l = len(target)
        dictionary = filter(lambda x: len(x) == l, dictionary)
        if len(dictionary) == 0:
            return str(l)
        # allabbr = self.generateAbbreviations(target)
        allabbr =  Queue.LifoQueue()
        allabbr.put((0, "", 0))
        res = Queue.PriorityQueue()
        while not allabbr.empty():
            pos, tmp, count = allabbr.get()
            if l == pos:
                tmp = tmp + (str(count) if count > 0 else "")
                res.put((len(tmp), tmp))
                
            else:
                allabbr.put((pos + 1, tmp + (str(count) if count > 0 else "") + target[pos], 0))
                allabbr.put((pos + 1, tmp, count + 1))
        
        while not res.empty():
            now = res.get()
            flag = True
            for w in dictionary:
                if self.validWordAbbreviation(w, now[1]):
                    flag = False
                    break
            if not flag:
                continue
            else:
                return now[1]
