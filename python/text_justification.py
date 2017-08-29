class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res, cur, numLetter = [], [], 0
        for w in words:
            if numLetter + len(w) + len(cur) > maxWidth:
                if len(cur) == 1:
                    res.append(cur[0] + ' ' * (maxWidth - numLetter))
                else:
                    space = maxWidth - numLetter
                    gap, extra = divmod(space, len(cur) - 1)
                    for i in range(extra):
                        cur[i] += ' '
                    res.append((' ' * gap).join(cur))
                cur, numLetter = [], 0
            cur.append(w)
            numLetter += len(w)
        res.append(' '.join(cur) + ' ' * (maxWidth - numLetter - len(cur) + 1))
        return res
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        tmp = 0
        res = []
        tw = []
        for c in words:
            if tmp + len(c) <= maxWidth:
                tmp += (len(c) + 1)
                tw.append(c)
            else:
                res.append(tw) 
                tmp = len(c) + 1
                tw = [c]
        res.append(tw)
        ret = []
        k = 0
        for it in res:
            k+=1
            t = len(it)
            if t == 1:
                ret.append(it[0] + ' ' * (maxWidth - len(it[0])))
            else:
                gapnum = len(it) - 1
                spacenum = maxWidth - sum([len(x) for x in it])
                gapsize = spacenum / gapnum
                ext = spacenum % gapnum
                tmp = ""
                if not(it[-1][-1] == '.' and k == len(res)):
                    for i in range(len(it)-1):
                        if i < ext:
                            tmp = tmp + it[i] + ' ' * (gapsize + 1)
                        else:
                            tmp = tmp + it[i] + ' ' * gapsize
                    tmp += it[-1]
                else:
                    tmp = " ".join(it)
                    if it[-1][-1] == '.':
                        print tmp, it
                    tmp += " " * (maxWidth - len(tmp))
                ret.append(tmp)
        return ret
