import Queue
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        times = []
        strs = []
        now = 0
        while now < len(s):
            if s[now].isdigit():
                tmp = 0
                while s[now].isdigit():
                    tmp = tmp * 10 + int(s[now])
                    now += 1
                times.append(tmp)
            elif s[now] == '[':
                strs.append(res)
                res = ""
                now += 1
            elif s[now] == ']':
                tmp = strs.pop()
                ti = times.pop()
                tmp += res * ti
                res = tmp
                now += 1
            else:
                res += s[now]
                now += 1
        return res
