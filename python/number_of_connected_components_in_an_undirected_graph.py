class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        dic = {}
        for i in range(n):
            dic[i] = []
        for x, y in edges:
            dic[x].append(y)
            dic[y].append(x)
        res = 0
        close ={}
        for i in range(n):
            if i not in close:
                stack = [i]
                close[i] = True
                res += 1
                while len(stack) > 0:
                    now = stack.pop()
                    for v in dic[now]:
                        if v not in close:
                            close[v] = True
                            stack.append(v)
        return res
