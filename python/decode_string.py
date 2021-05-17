    class Solution(object):
        def decodeString(self, s):
            """
            :type s: str
            :rtype: str
            """
            def decode(ind):
                level = num = 0
                ss = ''
                while ind < len(s):
                    if s[ind] == '[':
                        level += 1
                        a, ind = decode(ind + 1)
                        ss += a * num
                        num = 0
                    elif s[ind] == ']':
                        if level > 0:
                            level -= 1
                        else:
                            return ss, ind - 1
                    elif s[ind].isdigit():
                        num *= 10
                        num += int(s[ind])
                    else:
                        ss += s[ind]
                    ind += 1
                return ss, ind
            return decode(0)[0]
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
