import Queue
class Solution(object):
    def check(self, k, dic, m, n):
        q = Queue.LifoQueue()
        q.put((k, {k: True}, 1))
        ret = 0
        while not q.empty():
            now, path, dep = q.get()
            if m <= dep <= n:
                ret += 1
            if dep >= n:
                continue
            for i in range(1, 10):
                if i in path:
                    continue
                if i in dic[now]:
                    if dic[now][i] in path:
                        t = path.copy()
                        t.update({i: True})
                        q.put((i, t, dep + 1))
                else:
                    t = path.copy()
                    t.update({i: True})
                    q.put((i, t, dep + 1))
        return ret

    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dic = {1: {3: 2, 7: 4, 9: 5}, 3: {1: 2, 7: 5, 9: 6}, 7: {1: 4, 3: 5, 9: 8}, 9: {1: 5, 3: 6, 7: 8},
               2: {8: 5}, 4: {6: 5}, 6: {4: 5}, 8: {2: 5}, 5: {}}
        res = self.check(1, dic, m, n) * 4 + self.check(2, dic, m, n) * 4 + self.check(5, dic, m, n)
        return res

