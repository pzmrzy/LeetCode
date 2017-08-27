class Solution(object):
    res = 0
    tmp = 0

    def dfs(self, tree, depth, pos):
        self.tmp += tree[depth][pos]
        if depth == 3:
            self.res += self.tmp
            self.tmp -= tree[depth][pos]
            return
        if tree[depth + 1][pos * 2] == -1 and tree[depth + 1][pos * 2 + 1] == -1:
            self.res += self.tmp
            self.tmp -= tree[depth][pos]
            return
        if tree[depth + 1][pos * 2] != -1:
            self.dfs(tree, depth + 1, pos * 2)
        if tree[depth + 1][pos * 2 + 1] != -1:
            self.dfs(tree, depth + 1, pos * 2 + 1)
        self.tmp -= tree[depth][pos]

    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tree = [[-1] * 8 for _ in range(4)]
        for n in nums:
            V = n % 10
            n /= 10
            P = n % 10
            D = n / 10
            tree[D - 1][P - 1] = V
        self.dfs(tree, 0, 0)
        return self.res
