import bisect
from collections import deque

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        tmp = bisect.bisect_left(arr, x)
        l = len(arr)
        if tmp == l:
            left = right = l - 1
        elif arr[tmp] == x:
            left = right = tmp
        else:
            if tmp == 0:
                left = right = 0
            else:
                if x - arr[tmp - 1] <= arr[tmp] - x:
                    left = right = tmp - 1
                else:
                    left = right = tmp
        res = deque()
        res.append(arr[left])

        while len(res) < k:
            if left - 1 < 0:
                right += 1
                res.append(arr[right])
                continue

            if right + 1 == l:
                left -= 1
                res.appendleft(arr[left])
                continue

            if x - arr[left - 1] <= arr[right + 1] - x:
                left -= 1
                res.appendleft(arr[left])
            else:
                right += 1
                res.append(arr[right])
        return list(res)
