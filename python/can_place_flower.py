class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        num = 0
        l = len(flowerbed)
        if l == 1:
            return n == 0 or (flowerbed[0] == 0 and n == 1)
        if flowerbed[0] + flowerbed[1] == 0:
            flowerbed[0] = 1
            num += 1
        for i in range(1, l - 1):
            if flowerbed[i - 1] + flowerbed[i] + flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                num += 1
        if flowerbed[-1] + flowerbed[-2] == 0:
            num += 1
        return num >= n
