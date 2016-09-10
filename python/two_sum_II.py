class Solution(object):
    def find(self, num, t, l, r):
        n = len(num)-1
        while True:
            if (l+1 >= r):
                if num[l] == t:
                    return (True, l)
                if num[r] == t:
                    return (True, r)
                return (False, 0)
            m = (l+r)/2
            if num[m] == t:
                return (True, m)
            if num[m] < t:
                l = min(m + 1, n)
            else:
                r = max(0, m - 1)
           
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        for i in range(n):
            t = target - numbers[i]
            l = i + 1
            r = n - 1
            r = self.find(numbers, t, l, r)
            if r[0]:
                return [i + 1, r[1] + 1]
