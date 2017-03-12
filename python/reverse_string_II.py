class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ""
        l = len(s)
        now = 0
        flag = True
        while (now < l):
            if flag:
                if (now + k < l):
                    res += s[now:now + k][::-1]
                else:
                    res += s[now:][::-1]
            else:
                if (now + k < l):
                    res += s[now:now+k]
                else:
                    res += s[now:]
            now += k
            flag = not flag
        return res
